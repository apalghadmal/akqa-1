import logging
import pytest
from selenium import webdriver

from Utils import utils
from pytest_bdd import (
    given,
)


def pytest_addoption(parser):
    """get parameters from command line using fixture function
    Args:
        parser (TYPE): Description
    """
    parser.addoption("--config", action="store", nargs='?',
                     type=str, default='config.base',
                     help='the config you\'d like to use')

    parser.addoption("--host", action="store",
                      help='Specify a myps url')

    parser.addoption("--browser", action="store",
                     help='Specify a browser')

    parser.addoption("--timeout", action="store",
                     help='Specify time to wait for conditions to be \
                         satisfied in browser')

    parser.addoption("--hub", action="store", nargs='?',
                      help="specify the selenium hub")

    parser.addoption("--remote",action="store",
                      help="Specify remote true or false")


@pytest.fixture ()
def getUrl():
    getUrl = "https://www.jagermeister.com/en/home"
    return getUrl

@pytest.fixture()
def getHost(request):
    Host = utils.get_config_var('host',
                                  utils.process_config_file(request))
    return Host

@pytest.fixture
def base_url(request):
    """Set fixture of BASE_URL to provided argument or default
    Args:
        request (object): conftest object to introspect test environment
    """
    global base_alternate_url
    _base_url = request.config.getoption("--host")
    if not _base_url:
        _base_url = utils.get_config_var('host',
                                         utils.process_config_file(request))
    return _base_url


@pytest.fixture
def browser_type(request):
    """Set fixture of browser_type to provided argument or default
    Args:
        request (object): conftest object to introspect test environment
    """
    _browser = request.config.getoption("--browser")
    if not _browser:
        _browser = utils.get_config_var('browser',
                                        utils.process_config_file(request))
    return _browser


@pytest.fixture
def timeout(request):
    """Set fixture of timeout to provided argument or default
    Args:
        request (object): conftest object to introspect test environment
    """
    _timeout = request.config.getoption("--timeout")
    if not _timeout:
        _timeout = utils.get_config_var('timeout',
                                        utils.process_config_file(request))
    return _timeout


@pytest.fixture
def hub(request):
    """Return a hub url
    Args:
        request (object): conftest object to introspect test environment
    """
    _hub = request.config.getoption("--hub")
    if not _hub:
        _hub = utils.get_config_var('hub',
                                    utils.process_config_file(request))
    return _hub


@pytest.fixture
def remote(request):
    """Returns remote true or false.
    Args:
        request (object): conftest object to introspect test environment
    """
    _remote = request.config.getoption("--remote")
    if not _remote:
        _remote = utils.get_config_var('remote',
                                    utils.process_config_file(request))
    return _remote


@pytest.yield_fixture
def driver(request, browser_type,hub,remote):
    utils.init_logging()
    logger = logging.getLogger(__name__)
    logger.info('*************************')
    logger.info('Starting tests for %s', request.module.__name__)
    logger.info('*************************\n')
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-infobars")
        if remote is False:
            _driver = webdriver.Chrome(chrome_options=options)  # getattr(webdriver, browser_type)()
        else:
            _driver = webdriver.Remote(command_executor= hub, desired_capabilities=options.to_capabilities())  # getattr(webdriver, browser_type)()
    except AttributeError as error:
        logger.info("Browser type %s unavailable!", browser_type)
        logger.exception(error)
        url = 'https://seleniumhq.github.io/docs/start.html#consumer_browsers'
        logger.info("Review %s for available browsers", url)
        raise AttributeError
    _driver.set_window_position(0, 0)
    _driver.set_window_size(1400, 900)
    _driver.maximize_window()
    request.node._driver = _driver
    yield _driver
    _driver.quit()


@given("User access website homepage")
def valid_login(driver):
    logger = logging.getLogger(__name__)
    logger.info('Default valid log in with provided username and password')
    driver.get("https://www.jagermeister.com/en-GB/home")

