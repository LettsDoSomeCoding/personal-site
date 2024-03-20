from diagrams import Cluster, Diagram
from diagrams.programming.flowchart import Action,Decision,InputOutput,StartEnd
from diagrams.c4 import Container

with Diagram("Development Workflow", filename="dev-workflow"):
    with Cluster("Development Environment"):
        devcontainer = Container(
            name="devcontainer",
            technology="VSCode devcontainer and Docker",
            description="Containerised dev environment for consistency and simplicity"
        )

        IDE = Container(
            name="IDE",
            technology="VSCode",
            description="Required to use the devcontainer natively (there is an option just to use the dockerfile with other IDEs)"
        )

    codePush=Decision("Push Code to GitLab")

    codeMirror=Decision("Code mirrored to GitHub from GitLab")

    contIntTrigger=Action("GitLab CI triggered off of code push")

    IDE >> codePush >> contIntTrigger
    codePush >> codeMirror
