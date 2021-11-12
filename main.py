import server

app = server.create_app()

app.run("localhost", port=4200)
