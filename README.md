# flask-watchlist

A simple Flask REST API that allows you to track your movie watchlist.

> Want to learn how to build this and deploy it to [Back4app Containers](https://www.back4app.com/container-as-a-service-caas)? Check out the [article](https://blog.back4app.com/what-are-containers-in-cloud-computing/).

## Development

1. Fork/Clone

2. Create and activate a virtual environment:

    ```sh
    $ python3 -m venv venv && source venv/bin/activate
    ```

3. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```

4. Initialize the database:

    ```sh
    (venv)$ python init_db.py
    ```

5. Run the server:

    ```sh
    (venv)$ flask run
    ```
    
 6. Navigate to [http://localhost:5000/](http://localhost:5000/) in your favorite web browser.

## Deploy (Docker)

1. Install Docker (if you don't have it yet).

2. Build and tag the image:
    ```sh
    (venv)$ docker build -t flask-watchlist:1.0 .
    ```

3. Start a new container:
   ```sh
    (venv)$ docker run -it -p 5000:5000 -d flask-watchlist:1.0
    ```

4. Navigate to [http://localhost:5000/](http://localhost:5000/) in your favorite web browser.
