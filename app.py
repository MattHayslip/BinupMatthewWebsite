from main_website import run_app
from main_website import  Config, DevelopmentConfig, ProductionConfig
from main_website.lib.util import error, success, update_packages

APP = run_app()

def run():
    try:
        APP.run(
            # to handle multiple requests at the same time
            threaded = ProductionConfig.Threaded, # allow to run on multiple threads
            debug    = DevelopmentConfig.DEBUG,   # auto reload server
            port     = Config.port,               # the port where the app is being served on 
            host     = Config.apphost             # run online using my PC ip
        )
    except Exception as e:
        print(f" * {error}error <-- main: {str(e)}")


if __name__ == '__main__':
    # update_packages() # TODO: Comment out for the deployment
    run()