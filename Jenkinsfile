pipeline {
    agent any

    stages {
        stage('ansible stage') {
            agent {
                label 'ansible'
            }
            steps {
                sh '''
                git clone https://github.com/Mohan14242/A1.git
                cd A1
                '''
            }
        }

        stage("Terraform stage") {
            agent{
                label 'terraform'
            }
            steps {
               sh '''
               git clone https://github.com/Mohan14242/T1.git
               cd T1

                '''
            }
        }
    }
}
