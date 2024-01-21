pipeline {
    agent any

    stages {
        stage('Build') {
            agent {
                label 'ansible'
            }
            steps {
                script {
                    git clone url: 'https://github.com/Mohan14242/jenkins2.git'
                 
                        // Add more Ansible commands or other build steps here if needed
                    }
                }
            }
        }
    


        stage("testting stage"){
            steps{
                script{
                    echo "this is the chiru who are you"
                }
            }
        }
    }
}
