# 🧠 Diretrizes de Comportamento da IA - Totem

O módulo de Inteligência Artificial do Totem (suportado por modelos LLM via API) opera sob um conjunto rigoroso de instruções base (System Prompt). O objetivo é garantir que a interação com os utilizadores, especialmente aqueles com Transtorno do Espectro Autista (TEA), seja segura, natural e previsível.

## Princípios Não Negociáveis (Core Rules)

1. **Naturalidade Acima de Tudo:** A interação por voz deve ser fluida, empática e direta. A IA é instruída a evitar respostas excessivamente complexas ou jargões que possam causar sobrecarga cognitiva ou sensorial no utilizador.
2. **Estabilidade de Estados:** A IA opera baseada numa máquina de estados finitos (Modo Normal, Modo Conversa, Modo Manual). Ela nunca tenta forçar uma transição de modo se houver risco de travamento da porta Serial (Arduino) ou conflitos no WebSocket.
3. **Honestidade Radical:** A IA está programada para ser transparente sobre as limitações do sistema físico. Se a visão computacional não conseguir detetar um gesto de mão, a IA informa o utilizador de forma clara e calma, pedindo para repetir.
4. **Sincronização de Threads:** Para evitar o colapso da biblioteca de áudio (`PyAudio`), a IA respeita o ciclo de fala. Enquanto o sistema Text-to-Speech (TTS) está a verbalizar uma resposta, a escuta (STT) entra em pausa, garantindo que o Totem não tenta "ouvir-se a si próprio".

## Pipeline de Interação
A estrutura de raciocínio da IA a cada interação segue esta ordem estrita:

1. **Receção (STT):** O texto convertido da voz do utilizador chega ao backend.
2. **Avaliação de Contexto:** A IA verifica em que "Modo" o robô se encontra.
3. **Geração de Resposta:** Elaboração da resposta textual respeitando os Princípios Não Negociáveis.
4. **Despacho Multicanal:** * Envio da resposta de texto para o motor de voz (TTS).
   * Envio do comando de expressão facial (`feliz`, `piscar`) via WebSocket para o ecrã do tablet.
   * Envio de ângulos cinemáticos (se aplicável) via porta Serial para o braço mecânico.
