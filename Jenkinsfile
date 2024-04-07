pipeline{
    agent any 
    stages{
        stage("mohan"){
            timeout(time:1,unit:"MINUTES",messsage:"this has timeout")
            steps{
                script{
                    sh'sleep 100'
                }
            }
        }
        stage("chiru"){
            timeout(time:1,unit:"MINUTES",skip:true)
            steps{
                script{
                    sh "sleep 100"
                }
            }
        }

        
    }
}