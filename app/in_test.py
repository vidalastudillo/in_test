""" ----------------------------------------------------------------------------
Purpose
--------------------------------------------------------------------------------

Provide a simple container to test deployments.

--------------------------------------------------------------------------------
Details
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
Versions
--------------------------------------------------------------------------------

26 dec 2021:
- First draft started.

---------------------------------------------------------------------------- """


__version__ = '0.0.4-Beta'
__author__ = 'Mauricio Vidal, VIDAL & ASTUDILLO Ltda.'


# Standard requirements
import logging


# Third parties requirements
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


# V&A requirements
from va_time.va_time import (
    get_now_in_seconds,
)


# Logger configuration
logger_test = logging.getLogger(__name__)
logger_test.setLevel(logging.DEBUG)
# logger_test.setLevel(logging.INFO)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)


app = FastAPI(
    title="Test App",
    description="This is a test App",
    version=__version__
)


@app.get("/")
def read_root() -> HTMLResponse:
    """
    Displays the home, with some useful information.
    """
    content = f"""
        <body>
        <p>Hello world!</p>
        <p>This App has version: {__version__}</p>
        <p>{get_now_in_seconds()}</p>
        </body>
        <footer>
        <p>VIDAL & ASTUDILLO Ltda, 2016-2022<br>www.vidalastudillo.com</p>
        </footer>
    """
    return HTMLResponse(content=content)


if __name__ == '__main__':
    import uvicorn

    # print("\033c")

    uvicorn.run(app, host="0.0.0.0", port=8081)  # nosec
