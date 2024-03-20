from diagrams import Cluster, Diagram
from diagrams.c4 import Container, Person, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram(
    name="Development Workflow",
    filename="docs/dev-workflow",
    direction="TB",
    graph_attr=graph_attr,
    show=False,
):
    with Cluster("Development Environment"):
        devcontainer = Container(
            name="Devcontainer",
            technology="VSCode devcontainer and Docker",
            description="Containerised dev environment for consistency and simplicity",
            width="3",
        )

        IDE = Container(
            name="IDE",
            technology="VSCode",
            description="Required to use the devcontainer natively (there is an option just to use the dockerfile with other IDEs)",
            width="3",
        )

        developer = Person(name="Developer")

    gitlabRepo = Container(
        name="GitLab Code Repository",
        width="2.5",
    )

    githubRepo = Container(
        name="GitHub Code Repository",
        width="2.5",
    )

    with Cluster("Continuous Integration"):
        buildContainer = Container(
            name="Build Container",
            technology="Docker",
            description="Container image used in CI to build and deploy website",
            width="3",
        )

        gitlabCI = Container(
            name="CI Pipeline",
            technology="GitLab CI",
            description="Continuous integration and deployment pipeline to build and publish website",
            width="3",
        )

    website = Container(
        name="Personal Website",
        technology="Hugo, GitLab Pages",
        description="Static website built using Hugo and deployed onto GitLab Pages",
    )

    (
        developer
        >> Relationship("Code is pushed from local IDE to GitLab Repo")
        >> gitlabRepo
    )
    gitlabRepo >> Relationship("GitLab Repo is push-mirrored to GitHub") >> githubRepo
    (
        gitlabRepo
        >> Relationship("GitLab CI is triggered upon a commit to the main branch")
        >> gitlabCI
    )
    gitlabCI >> Relationship("GitLab CI builds the website and deploys it") >> website
