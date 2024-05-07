---
title: Homepage
type: landing

cascade:
- _target:
    kind: page
    lang: en
    path: /post/**
  params:
    commentable: true

sections:
  - block: about.biography
    id: about
    content:
      title: Biography
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
    # Showcase personal skills or business features.
  - block: features
    content:
      title: Skills
      subtitle: My proficiency level for different technologies
      # Add/remove as many `feature` blocks below as you like.
      items:
        - name: "Python"
          icon: "python"
          icon_pack: "icomoon"
          description: "60%"
        - name: "C#"
          icon: "csharp"
          icon_pack: "icomoon"
          description: "70%"
        - name: "Linux"
          icon: "linux"
          icon_pack: "icomoon"
          description: "60%"  
        - name: "Terraform"
          icon: "terraform"
          icon_pack: "icomoon"
          description: "50%"
        - name: "GitLab CI and Admin"
          icon: "gitlab"
          icon_pack: "icomoon"
          description: "90%" 
        - name: "Git"
          icon: "git"
          icon_pack: "icomoon"
          description: "70%"
        - name: "Grafana and Prometheus Monitoring and Alerting"
          icon: "prometheus"
          icon_pack: "icomoon"
          description: "75%"
        - name: "Kubernetes"
          icon: "kubernetes"
          icon_pack: "icomoon"
          description: "30%"
        - name: "Puppet"
          icon: "puppet"
          icon_pack: "icomoon"
          description: "80%"
  - block: collection
    id: posts
    content:
      title: Recent Posts
      subtitle: ''
      text: 'Check out my recent blog posts below!'
      # Choose how many pages you would like to display (0 = all pages)
      count: 5
      # Filter on criteria
      filters:
        # The folders to display content from
        folders:
          - post
        author: ""
        category: ""
        tag: ""
        publication_type: ""
        featured_only: false
        exclude_featured: false
        exclude_future: false
        exclude_past: false
      # Choose how many pages you would like to offset by
      # Useful if you wish to show the first item in the Featured widget
      offset: 0
      # Field to sort by, such as Date or Title
      sort_by: 'Date'
      sort_ascending: false
    design:
      # Choose a listing view
      view: compact
      # Choose single or dual column layout
      columns: '2'
  - block: contact
    id: contact
    content:
      title: Contact
      subtitle: ''
      text: ''
    #   Contact details - edit or remove options as needed
    #   email: owen.letts@gmail.com
    #   phone: 888 888 88 88
    #   appointment_url: 'https://calendly.com'
    #   address:
    #     street: 450 Serra Mall
    #     city: Stanford
    #     region: CA
    #     postcode: '94305'
    #     country: United States
    #     country_code: US
    #   directions: Enter Building 1 and take the stairs to Office 200 on Floor 2
    #   office_hours:
    #     - 'Monday 10:00 to 13:00'
    #     - 'Wednesday 09:00 to 10:00'
    #   contact_links:
        # - icon: twitter
        #   icon_pack: fab
        #   name: DM Me
        #   link: 'https://twitter.com/Twitter'
        # - icon: skype
        #   icon_pack: fab
        #   name: Skype Me
        #   link: 'skype:echo123?call'
        # - icon: video
        #   icon_pack: fas
        #   name: Zoom Me
        #   link: 'https://zoom.com'
      # Automatically link email and phone or display them just as text?
      autolink: true
      # Choose an email form provider (netlify/formspree)
      form:
        provider: formspree
        formspree:
          # If using Formspree, enter your Formspree form ID
          id: 'https://formspree.io/f/owen.letts@gmail.com'
      # Coordinates to display a map - set your map provider in `params.yaml`
      coordinates:
        latitude: '50.9103'
        longitude: '-1.4048'
    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '1'
---