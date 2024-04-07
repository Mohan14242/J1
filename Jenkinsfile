pipeline{
    agent any 
    options{
        timeout(time:2,unit:"MINUTES")
    }
    stages{
        stage("mohan"){
            options{
            timeout(time:1,unit:"MINUTES")
            }
            steps{
                script{
                    sh'sleep 100'
                }
            }
        }
        stage("chiru"){
            options{
            timeout(time:1,unit:"MINUTES")
            }
            steps{
                script{
                    sh "sleep 100"
                }
            }
        }

        
    }
}