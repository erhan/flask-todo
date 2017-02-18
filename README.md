#  Flask Örnek Todo Uygulaması

[![python](https://img.shields.io/badge/python-3.5-blue.svg)]() [![flask](https://img.shields.io/badge/built%20with-flask-yellow.svg)](https://github.com/pallets/flask)


----------

#### Kurulum

1. Github'tan clone edin. 
    ```
    $ git clone https://github.com/erhan/flask-todo
    ```
    
1. Virtualenv klasörünü oluşturun.
    ```
    $ virtualenv -p python3.5 env
    ```

2. Gerekli modülleri `requirements.txt` dosyasından kurun.
    ```
    $ env/bin/pip install -r requirements.txt
    ```
    
3. Veritabanını güncelleyin.(Default kullanıcı oluşturur.)
    ```
    $ env/bin/python migrate.py db upgrade
    ```
    
3. Uygulamayı çalıştırın
    ```
    $ env/bin/python run.py
    ```

----------
