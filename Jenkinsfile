pipeline{
    agent {node { label "terraform1"}}
    environment{
        package=''
    }
    stages{
        stage("getting the version of the file "){
            steps{
                def package=readJSON file="package.json"
                def version=package.verion 
                script{
                    echo "in this we are getting the software version"
                }



            }
            
        }
        stage("printing the version"){
            steps{
                script{
                    sh '''
                    the package version is ${package}'''
                }
            }



        }
    }
}