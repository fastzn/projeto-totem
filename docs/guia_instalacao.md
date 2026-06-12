# 🛠️ Guia de Instalação e Execução - Projeto Totem

Este guia destina-se a investigadores e engenheiros que desejem replicar ou testar o ambiente de software e hardware do Projeto Totem.

## Pré-requisitos
* **Python 3.10+** instalado no sistema.
* **Arduino IDE** (para compilação do firmware do microcontrolador).
* Conta ativa na **Groq** para geração da chave de API (Llama 3.1).

## Passo 1: Preparar o Hardware (Firmware)
1. Abra o ficheiro `/software/firmware/totem.ino` no Arduino IDE.
2. Aceda ao Gestor de Bibliotecas e instale a dependência `Adafruit PWM Servo Driver Library`.
3. Conecte o Arduino Uno via USB, compile e carregue o código.
4. Anote a porta de comunicação (ex: `COM3` no Windows ou `/dev/ttyUSB0` no Linux/Mac).

## Passo 2: Configurar o Backend (Cérebro do Sistema)
1. Abra um terminal e navegue até à pasta do backend:
   ```bash
   cd software/backend
