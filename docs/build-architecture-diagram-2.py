from diagrams import Cluster, Diagram
from diagrams.c4 import Container, Person, Relationship

with Diagram("Development Workflow", filename="docs/dev-workflow"):
    with Cluster("Development Environment"):
        devcontainer = Container(
            name="devcontainer",
            technology="VSCode devcontainer and Docker",
            description="Containerised dev environment for consistency and simplicity",
        )

        IDE = Container(
            name="IDE",
            technology="VSCode",
            description="Required to use the devcontainer natively (there is an option just to use the dockerfile with other IDEs)",
        )
        
        developer = Person(name="Developer")
    
    gitlabRepo = Container(
        name="GitLab Code Repository",
        description="GitLab is used as the main repository as GitLab Pages is where the website will be deployed",
    )
    
    githubRepo = Container(name="GitHub Code Repository")        
    
    developer >> Relationship("Code is pushed from local IDE to GitLab Repo") >> gitlabRepo
    gitlabRepo >> Relationship("GitLab Repo is push-mirrored to GitHub") >> githubRepo