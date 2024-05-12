pipeline {
    agent any  
    parameters{
        string(name: "param1", defaultValue: "default_value1", description: "Parameter 1 description")
        booleanParam(name: "param3", defaultValue: true, description: "Parameter 3 description")
    }
    stages{
        stage("testing the statge"){
            steps{
                script{
                    echo "the parameters are ${params.param1}"
                    echo "the second parameter is ${params.param2}"
                    echo "the thidrd parameters is ${params.param3}"

            }
            }
        }
        stage("installing snyk"){
            steps{
                sh '''
                npm install -g snyk
                '''
            }
        }

        stage('snyk stage'){steps {
                withCredentials([string(credentialsId: 'snyk-api-token', variable: 'SNYK_TOKEN')]) {
                    sh "snyk test --all-projects --json --org=mohan14242"
                }

        }
    }
}
}