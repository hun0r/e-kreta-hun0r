@echo off

REM Build the package
echo Building the package...
python setup.py sdist bdist_wheel
if %errorlevel% neq 0 (
    echo Failed to build the package.
    exit /b %errorlevel%
)

REM Install the package locally
echo Installing the package...
pip install dist\e_kreta-0.1-py3-none-any.whl
if %errorlevel% neq 0 (
    echo Failed to install the package.
    exit /b %errorlevel%
)

REM Create a test script outside the package directory
echo Creating test script...
echo
echo from e_kreta.api.kreta_api import Session
echo.
echo def main():
echo     username = 'your_username'
echo     password = 'your_password'
echo     klik = 'your_klik'
echo.
echo     session = Session.login(username, password, klik)
echo     print("Logged in successfully")
echo.
echo     try:
echo         student_data = session.getStudent()
echo         print("Student Data:", student_data)
echo.
echo         evaluations = session.getEvaluations()
echo         print("Evaluations:", evaluations)
echo.
echo         lep_events = session.getLEPEvents()
echo         print("LEP Events:", lep_events)
echo     finally:
echo         session.close()
echo         print("Session closed")
echo.
echo if __name__ == "__main__":
echo     main()
> test_installation.py

REM Run the test script
echo Running test script...
python test_installation.py
if %errorlevel% neq 0 (
    echo Test script failed.
    exit /b %errorlevel%
)

REM Cleanup build artifacts
echo Cleaning up...
rd /s /q build
rd /s /q dist
rd /s /q e_kreta.egg-info

echo Done!
pause
