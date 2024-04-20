@Library('mohan') _

pipeline {
    agent any
    
    stages {
        stage('Example') {
            steps {
                script {
                    def values=[1,2,3,4,5,6,7,8]
                    chiru.list_values(values)

                }
            }
        }
    }
}
