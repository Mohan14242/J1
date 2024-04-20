@Library('mohan') _

pipeline {
    agent any
    
    stages {
        stage('Example') {
            steps {
                script {
                    def maps=["name":"mohan","age":25,"salary":30000]
                    chiru.names() // Call the 'names' function from the shared library
                    mohan.exam()
                }
            }
        }
    }
}
