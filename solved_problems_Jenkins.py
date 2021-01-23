#  How  to run regresion tests with pytest connection to Git

#  use : 'Pyenv Pipeline' plugin (https://plugins.jenkins.io/pyenv-pipeline)
"""
stage("test PythonEnv") {

    withPythonEnv('python3') {
        sh 'pip install pytest'
        sh 'pytest mytest.py'
    }
}
"""

#  OR
"""
node
{
   stage('Run pytest') 
   {
       bat "pytest mytest.py"
   }    
}
"""
