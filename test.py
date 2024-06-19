from e_kreta.api.kreta_api import Session

def main():
    # Replace with actual credentials for testing
    username = 'your_username'
    password = 'your_password'
    klik = 'your_klik'

    session = Session.login(username, password, klik)
    print("Logged in successfully")
    
    try:
        student_data = session.getStudent()
        print("Student Data:", student_data)

        evaluations = session.getEvaluations()
        print("Evaluations:", evaluations)

        lep_events = session.getLEPEvents()
        print("LEP Events:", lep_events)
    finally:
        session.close()
        print("Session closed")

if __name__ == "__main__":
    main()
