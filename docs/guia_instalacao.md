# 🛠️ Guia de Instalação e Execução - Projeto Totem

Este guia destina-se a investigadores e professores que desejem replicar ou testar o ambiente de software e hardware do Projeto Totem.

## Pré-requisitos
* Python 3.10+ instalado no sistema.
* Arduino IDE (para compilação do firmware do microcontrolador).
* Conta ativa na Groq para geração da chave de API.

## 1: Preparar o Hardware (Firmware)
1. Abra o ficheiro `/software/firmware/totem.ino` no Arduino IDE.
2. Instale a biblioteca `Adafruit PWM Servo Driver Library`.
3. Conecte o Arduino Uno via USB e carregue o código.

## 2: Configurar o Backend (Cérebro do Sistema)
1. Instale as dependências rigorosas do projeto usando o arquivo `requirements.txt`.
2. Crie um ficheiro oculto chamado `.env` e insira a sua chave de API para habilitar a IA.
3. Atualize a porta Serial no código para conectar ao Arduino.

## 3: Executar a Integração
1. Com o hardware ligado, inicie o servidor rodando o arquivo `main.py`.
2. Abra o ficheiro `/software/frontend/index.html` no navegador do tablet.
3. Clique no botão "Desbloquear Áudio" para superar o bloqueio do Android.
