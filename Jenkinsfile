pipeline{
    agent { node { label "agent1"}}
    stages{
        stage("build"){
            steps{
                echo 'this stage is bulding stage '

            }
        }
        stage("test"){
            steps{
                echo "this stage is test stage"
            }
        }
        stage("plan"){
            steps{
                echo "this is teh plan stage"
            }
        }
    }
}