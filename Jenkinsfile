@Library('mohan') _

pipeline {
    agent any
    
    stages {
        stage('Example') {
            steps {
                script {
                    def configmap = [application: "catalogue", component: "catalogue"]
                    mohan.names(configmap) // Call the 'names' function from the 'mohan' shared library
                }
            }
        }
    }
}
