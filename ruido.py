import numpy as np

def gerar_ruido_rosa(tamanho):
    """
    Gera ruído rosa com base no método de filtragem em frequência.
    """
    frequencias = np.fft.rfftfreq(tamanho, d=1.0)
    frequencias[0] = frequencias[1]  # Evitar divisão por zero
    amplitude = 1 / (frequencias**(1 / 2.0))  # Decaimento de 3 dB por oitava
    fases = np.exp(2j * np.pi * np.random.rand(len(frequencias)))
    espectro = amplitude * fases
    ruido_rosa = np.fft.irfft(espectro)
    ruido_rosa = ruido_rosa[:tamanho] / np.max(np.abs(ruido_rosa))  # Normalizar
    return ruido_rosa

def gerar_ruidos(audio, taxa_amostragem, intensidade_branco=0.02, intensidade_rosa=0.02, intensidade_impulso=0.005, intensidade_harmonico=0.005):
    duracao = len(audio) / taxa_amostragem

    # Ruído branco
    ruido_branco = intensidade_branco * np.random.normal(0, 1, size=len(audio))

    # Ruído rosa
    ruido_rosa = intensidade_rosa * gerar_ruido_rosa(len(audio))

    # Ruído de impulsos
    ruido_impulso = np.zeros_like(audio)
    indices_impulso = np.random.choice(len(audio), size=int(intensidade_impulso * len(audio)), replace=False)
    ruido_impulso[indices_impulso] = np.random.uniform(-0.5, 0.5, size=len(indices_impulso))

    # Ruído harmônico
    tempo = np.linspace(0, duracao, len(audio))
    ruido_harmonico = intensidade_harmonico * (np.sin(2 * np.pi * 400 * tempo) +
                                               np.sin(2 * np.pi * 800 * tempo) +
                                               np.sin(2 * np.pi * 1600 * tempo))

    # Áudio final
    audio_ruidoso = audio + ruido_branco + ruido_rosa + ruido_impulso + ruido_harmonico
    audio_ruidoso = audio_ruidoso / np.max(np.abs(audio_ruidoso))
    
    return audio_ruidoso