# ⚙️ Especificações de Hardware - Projeto Totem

Esta secção detalha a arquitetura física e eletrónica do Projeto Totem, desenvolvida com o rigor necessário para aplicações em engenharia mecatrónica e robótica assistiva.

## 📦 Bill of Materials (BOM)
- **Microcontrolador:** Arduino Uno R3
- **Driver de Servos:** Módulo Controlador PWM I2C PCA9685 (16 Canais, 12 bits)
- **Atuadores:** 6x Servomotores MG996R (Alto Torque, Engrenagens de Metal)
- **Interface Visual:** Tablet Red Pad 2 (Android)
- **Visão Computacional:** Webcam USB 480p
- **Fonte de Alimentação:** Fonte externa dedicada para os motores (5V/6A a 10A recomendado) para suportar o pico de corrente e evitar instabilidade no microcontrolador.

## 🔌 Diagrama de Ligações e Pinagem

### Arduino Uno <-> PCA9685
A comunicação entre o cérebro físico e o controlador de motores é feita via protocolo I2C:
* **Arduino 5V** -> PCA9685 VCC (Alimentação apenas da lógica do chip)
* **Arduino GND** -> PCA9685 GND
* **Arduino A4 (SDA)** -> PCA9685 SDA (Linha de Dados)
* **Arduino A5 (SCL)** -> PCA9685 SCL (Linha de Clock)

### Alimentação de Potência (PCA9685)
* **V+ / GND (Terminal Block):** Conectado diretamente à fonte de alimentação externa. 
> ⚠️ **Nota Crítica de Engenharia:** Nunca alimentar os motores MG996R diretamente pelo pino 5V do Arduino. O pico de corrente de um único MG996R em stall pode ultrapassar 1.5A, o que destruiria imediatamente o regulador de tensão do Arduino.

### Mapeamento Cinético (Servos)
De acordo com o firmware estabelecido em `/software/firmware/totem.ino`:
* **Canal 0:** Flexão do Polegar (Restrição mecânica: 0° a 70°, iterando em passos de 20° para evitar danos à engrenagem)
* **Canal 1:** Dedo Indicador
* **Canal 2:** Dedo Médio
* **Canal 3:** Dedo Anelar e Mínimo
* **Canal 5:** Rotação do Punho (Restrição de limite: 30° a 180°, onde 30° = Palma para cima, 100° = Posição neutra)

## 🖨️ Modelagem 3D (CAD/STL)
Os ficheiros de design paramétrico e malhas prontas para fatiamento encontram-se, respetivamente, nas subdiretorias `/cad` e `/stl`. O design foi estruturado para suportar a montagem em materiais poliméricos (PLA/ABS) com preenchimento adequado para suportar o torque dos servos MG996R sem comprometer a leveza estrutural.
