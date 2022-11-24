"""entry point"""
from distutils.log import debug
from main import create_app
from flask import request,make_response

# from src.uni import data_loader

app = create_app()



@app.after_request
def after_request_func(response):
    origin=request.headers.get("Origin")
    if request.method=="OPTIONS":
        response=make_response()
        response.headers.add("Access-Control-Allow-Credentials","true")
        response.headers.add("Access-Control-Allow-Headers","Content-Type")
        response.headers.add("Access-Control-Allow-Headers","x-csrf-token")
        response.headers.add("Acces-Control-Allow-Methods","GET,POST,OPTIONS,PUT,PATCH,DELETE")
        if origin:
            response.headers.add("Access-Control-Allow-Origin",origin)
    else:
        response.headers.add("Access-Control-Allow-Credentials","true")

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    print(app.url_map)
