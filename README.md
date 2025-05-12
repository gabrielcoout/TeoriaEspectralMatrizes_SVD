# 🎧 Análise Espectral de Áudio com SVD

**Análise Espectral de Áudio com SVD** é um projeto baseado em **Python** e **JupyterLab** que aplica a Transformada de Fourier de Curto Prazo (STFT) e a Decomposição em Valores Singulares (SVD) para compressão e reconstrução de sinais de áudio. A ideia é explorar a estrutura espectral do áudio, reduzindo sua dimensionalidade e visualizando a perda de informação com diferentes níveis de truncamento.

---

## 📌 **Recursos**
- 🎼 Carregamento e pré-processamento de arquivos `.wav`
- 🧠 Aplicação da SVD para compressão espectral
- 📊 Geração de gráficos (espectrogramas, histograma, proporção acumulada)
- 🔁 Reconstrução de áudio com diferentes valores de truncamento `k`
- 📉 Análise quantitativa: erro de reconstrução vs. taxa de compressão

---

## 📁 **Estrutura do Projeto**
```
📂 svd_atividade/
│── 📄 README.md                       # Documentação do projeto
│── 📄 requirements.txt                # Dependências Python
│── 📄 AtividadeTeoriaEspectral.ipynb  # Notebook principal
│── 📄 ruido.py                        # (Opcional) Manipulação de ruído
│── 📄 pdf2png.py                      # (Opcional) Conversão de PDF para imagens
│── 📂 audio/                          # Áudios originais e reconstruídos
│── 📂 img/                            # Gráficos e espectrogramas gerados
│── 📂 slides/                         # Arquivos de apresentação
```

---

## 🔧 **Instalação e Configuração**
> Recomendado o uso dentro de um ambiente virtual devido a restrições com `pip`.

1. **Crie e ative o ambiente virtual:**
   ```bash
   python3 -m venv jlab_env
   source jlab_env/bin/activate
   ```

2. **Instale as dependências:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## 🚀 **Como Usar**
1. **Inicie o JupyterLab:**
   ```bash
   jupyter-lab
   ```

2. **Abra o arquivo** `AtividadeTeoriaEspectral.ipynb` e execute as células para:
   - Carregar o áudio
   - Calcular a STFT
   - Aplicar a SVD
   - Visualizar espectrogramas truncados
   - Reconstruir e salvar os áudios
   - Analisar compressão vs qualidade

---

## ✅ **Resultados Esperados**
- Arquivos `.wav` reconstruídos para diferentes valores de `k`
- Espectrogramas comparativos (original vs truncados)
- Gráficos salvos na pasta `img/`:
  - Histograma de valores singulares
  - Proporção acumulada
  - Erro de reconstrução vs. `k`
  - Taxa de compressão

---

## 📌 **Próximos Passos**
- [ ] Classificação de audio usando PCA
- [ ] Exportação automática dos relatórios em PDF
- [ ] Aplicação em múltiplos áudios via batch

---

## 📬 **Contato**
Para dúvidas, sugestões ou contribuições, fique à vontade para abrir uma *issue* ou enviar um *pull request*.
