@Library('mohan') _

pipeline {
    agent any
    
    stages {
        stage('Example') {
            steps {
                script {
                    chiru.names() // Call the 'names' function from the shared library
                    mohan.exam()
                }
            }
        }
    }
}
