pipeline{
    agent any
    stages{
        stage("build"){
            agent { lable "agent1"}
            steps{
                sh '''
                ls -la'''

            }
        }
        stage("test"){
            agent { lable "agent2" }
            steps{
               script{
                ls -la
               }
            }
        }
        stage("plan"){
            steps{
                echo "this is teh plan stage"
            }
        }
    }
}