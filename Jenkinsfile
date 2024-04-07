pipeline{
    agent any
    stages{
        stage("build"){
            agent { label "agent1"}
            steps{
                sh '''
                ls -la'''

            }
        }
        stage("test"){
            agent { label "agent2" }
            steps{
               script{
                sh 'ls -la'
               }
            }
        }
        stage("plan"){
            step{
                echo "this is teh plan stage"
            }
        }
    }
    post{
        always{
            echo "this will always execute"
        }
        success{
            echo "this will run only if pipeline get sucess"
        }
        failure{
            echo "thiw will run only if the piepeline failyres"
        }
        changed{
            echo "these wwill executed only the result will changed"
        }
        aborted{
            echo "these will be exexuted only when pipelne is manually aborted"
        }
    }
}