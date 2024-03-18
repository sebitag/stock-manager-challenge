# Stock Manager Challenge

This challenge was made using the following projects as base:

- [FastApiBase](https://github.com/nanlabs/backend-reference/tree/main/examples/fastapi-base)
- [Vite boilerplate](https://github.com/emre-cil/vite-mui-ts)


## Steps to run locally

- Create the necessary `.env` files examples using the following examples
  - `.env.api.example`
    - Sign up [here](https://site.financialmodelingprep.com/developer/docs) to obtain your FMP API token.
  - `.env.frontend.example`
  - `.env.database.example` (**Note:** The value of `POSTGRES_HOST` should be the name of the db container.)
- Open your terminal on the root project directory
- Run the following command
  ```bash
  docker compose up --build
  ```
- After the containers are built, you should be able to access the app through
  ```
  http://localhost:3000/
  ```
- To access the API documentation navigate to
  ```bash
  http://localhost:8000/docs
  ```
- To access PGAdmin navigate to

  ```bash
  http://localhost:5050
  ```
  **Note:** PGAdmin credentials are in the `.env.database` file.