# TinyBug

TinyBug is a free, open-source, lightweight logging platform. It offers a straightforward alternative to Sentry, Logstash, and other similar services. Based purely on Python, and using MongoDB for storage, TinyBug provides a versatile logging solution for your applications.

TinyBug can be integrated seamlessly with a wide array of frameworks, including Django, Flask, FastAPI, Laravel, Spring, and more. It provides you with the tools to collect, analyze, and manage your application logs effectively and efficiently.

## Installation

To install TinyBug, you'll need Docker and Docker-Compose installed on your machine. Please follow the steps below to get it running:

1. **Clone the project**: Clone the repository to your local machine.

    ```
    git clone https://github.com/kaissb/tinybug.git
    ```

2. **Set up environment variables**: Rename the provided `.env.example` file to `.env` and modify the variables to fit your environment. Here's an example:

    ```
    # .env
    API_KEY=67e689be-858b-4e85-b526-de948a0efb1b
    PASSWORD=admin
    DATABASE_URL=mongodb://db:27017
    ```

3. **Build and run the Docker containers**: 

    ```
    docker-compose up --build
    ```

Your TinyBug application should now be up and running on your local machine at `localhost:80`.

## Usage

After installation, you can integrate TinyBug with your desired framework. The specifics of this process depend on the framework in use. More information about this will be provided soon.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## License

This project is licensed under the terms of the MIT license. See [LICENSE.md](LICENSE.md) for more details.
