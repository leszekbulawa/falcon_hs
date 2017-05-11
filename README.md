# Python Hacking - falcon

Projekt tworzony podczas spotkań *Python Hacking* w [Hacker:Space](http://hs3.pl/) trójmiasto.

## Pobranie i uruchomienie projektu

### Linux / MacOS

Pobranie źródeł i stworzenie virtualenv

```bash
mkdir -p ~/src/
mkdir -p ~/venv/

cd ~/src/
git clone git@github.com:hs3city/pythonhacking-falcon.git

python3.4 -m virtualenv ~/venv/pythonhacking-falcon

source ~/venv/pythonhacking-falcon/bin/activate

```

Instalacja zależności

```bash
cd ~/src/pythonhacking-falcon/
pip install --upgrade -r requirements.txt
```

Uruchomienie aplikacji

```bash
python main.py
```
