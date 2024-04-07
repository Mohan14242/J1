pipeline{
    agent any 
    stages{
        stage("mohan"){
            options{
            timeout(time:1,unit:"MINUTES",messsage:"this has timeout")
            }
            steps{
                script{
                    sh'sleep 100'
                }
            }
        }
        stage("chiru"){
            options{
            timeout(time:1,unit:"MINUTES",skip:true)
            }
            steps{
                script{
                    sh "sleep 100"
                }
            }
        }

        
    }
}