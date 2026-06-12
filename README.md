# Projeto Totem

O Projeto Totem é um assistente robótico interativo desenvolvido para atuar como uma tecnologia assistiva, especialmente para pessoas com Transtorno do Espectro Autista (TEA). O objetivo é auxiliar na interpretação de estímulos táteis e sociais. O sistema combina um braço mecânico, um rosto animado em um tablet, reconhecimento de voz e inteligência artificial para criar uma experiência de interação rica e responsiva.

## Arquitetura do Sistema

O projeto é dividido em três camadas principais:
* **Frontend (Tablet):** Interface desenvolvida em HTML5 e JavaScript que exibe o rosto animado e reproduz falas, comunicando-se via WebSocket.
* **Backend (Python):** Servidor Python 3.x que atua como motor de IA, processa reconhecimento de voz (STT), síntese de fala (TTS), visão computacional (rastreamento e detecção via MediaPipe/OpenCV) e controla os estados do robô.
* **Hardware (Arduino):** Controla os movimentos físicos do braço robótico recebendo comandos do servidor Python via comunicação serial USB.

## Componentes de Hardware

* Microcontrolador Arduino Uno.
* Controlador PWM PCA9685 de 16 canais.
* 6x Servos MG996R de alto torque.
* Tablet Red Pad 2 (Android) para a interface visual.
* Webcam USB 480p para visão computacional.

## Modos de Operação

* **Modo Normal:** O sistema aguarda o comando de ativação por voz.
* **Modo Conversa:** Processa comandos de voz, responde através da IA Groq (modelo Llama 3.1) e executa gestos.
* **Modo Manual:** Controle do braço através dos gestos da mão do usuário capturados pela webcam.
