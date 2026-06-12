"""
============================================================================
FICHEIRO: main.py
DESCRIÇÃO: Servidor principal (Cérebro do Totem) - Gere IA, Visão e Serial
DEPENDÊNCIAS: websockets, pyserial, pyaudio, mediapipe, opencv-python, groq
STATUS: ESTRUTURA BASE (MODULAR)
AUTOR: Pedro Antônio Leal Fernandes
============================================================================
"""
import asyncio
import websockets
import serial
import json

# ============================================================================
# CONFIGURAÇÃO DE HARDWARE (SERIAL)
# ============================================================================
# Ajuste a porta (ex: 'COM3' no Windows ou '/dev/ttyUSB0' no Linux)
PORTA_SERIAL = 'COM3' 
BAUD_RATE = 115200

try:
    arduino = serial.Serial(PORTA_SERIAL, BAUD_RATE, timeout=1)
    print("[HARDWARE] Arduino conectado com sucesso.")
except Exception as e:
    print(f"[AVISO] Arduino não detetado na porta {PORTA_SERIAL}: {e}")
    arduino = None

# ============================================================================
# FUNÇÕES DE CONTROLO DE MOTORES
# ============================================================================
def enviar_comando_braco(angulos):
    """
    Envia a string de ângulos no formato exigido pelo firmware.
    Exemplo de input: [70, 90, 90, 90, 0, 30] -> Output: $070090090090000030
    """
    if arduino:
        comando = "$" + "".join([f"{ang:03d}" for ang in angulos]) + "\n"
        arduino.write(comando.encode('utf-8'))
        print(f"[SERIAL] Comando enviado: {comando.strip()}")

# ============================================================================
# SERVIDOR WEBSOCKET (COMUNICAÇÃO COM O TABLET)
# ============================================================================
async def gerir_frontend(websocket, path):
    """ Gere a comunicação bidirecional com o rosto animado no tablet """
    print("[REDE] Tablet (Frontend) conectado via WebSocket.")
    try:
        async for mensagem in websocket:
            dados = json.loads(mensagem)
            print(f"[FRONTEND] Comando recebido: {dados}")
            
            # TODO: Integrar lógica da Groq (Llama 3.1) e PyAudio aqui
            # TODO: Integrar lógica de Visão Computacional (MediaPipe) aqui
            
    except websockets.exceptions.ConnectionClosed:
        print("[REDE] Tablet desconectado.")

# ============================================================================
# INICIALIZAÇÃO DO SISTEMA
# ============================================================================
async def iniciar_servidor():
    print("[SISTEMA] A iniciar o motor do Totem...")
    # Inicia o servidor na porta 8765
    async with websockets.serve(gerir_frontend, "0.0.0.0", 8765):
        await asyncio.Future()  # Mantém o servidor a correr infinitamente

if __name__ == "__main__":
    try:
        asyncio.run(iniciar_servidor())
    except KeyboardInterrupt:
        print("\n[SISTEMA] Servidor encerrado pelo utilizador.")
