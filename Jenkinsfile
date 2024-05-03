pipeline {
    agent any  
    parameters{
        string(name="PARAMETER_NAME",value="1.0.0")
    }
    stages{
        stage("testing the statge"){
            steps{
                script{
                    echo "the parameters are ${params.PARAMETER_NAME}"
            }
            }
        }
    }
}