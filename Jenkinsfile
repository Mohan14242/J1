@Library('mohan') _

pipeline {
    agent any
    
    stages {
        stage('Example') {
            steps {
                script {
                    mohan.names() // Call the 'names' function from the shared library
                }
            }
        }
    }
}
