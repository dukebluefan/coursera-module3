
def git_operation():
 print("I am adding example.py file to the remote repository.")

def test_git_operation():
    assert git_operation() == None

git_operation()
