pipeline{
    agent any 
    environment{
        user_details=credentials("ssh-auth")
    }
    stages{
        stage("printing the credentials"){
            script{
                script{
                    sh "the user_name is ${user_details_usr} and password is ${user_details_psw}"
                }
            }
        }

    }
}