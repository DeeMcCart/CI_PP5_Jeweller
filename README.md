# Jeweller 
Developer:  **Deirdre McCarthy**, Feb 2024

![Site image](./django_financial_planner/docs/readme_images/val-responsive.png?raw=true "Site image (responsive view)")


# Table of Contents:
1. [About](#about)
2. [Project Goals: ](#project-goals)
    1. [UX Design - Strategy ](#ux-design-strategy) 
    2. [UX Design - Strategy - Competitor Portals](#ux-design-strategy-analysis-of-competitors)
    3. [UX Design - Strategy - Target Audience](#ux-design-strategy-target-audience)
3. [UX Design - Scope](#ux-design-scope)
    1. [UX Design - Scope - User Requirements and Expectations](#ux-design-scope-user-requirements-and-expectations)
    2. [UX Design - Scope - Data](#ux-design-scope-data)
    3. [UX Design - Scope - Viewing Device](#ux-design-scope-viewing-device)
4. [User goals/ user stories: ](#user-goals-user-stories)
    1. [Site Owner Goals](#site-owner-goals)
    2. [First-time User Goals](#first-time-user-goals)
    3. [Returning User Goals](#returning-user-goals)
    4. [Other stakeholder Goals](#other-stakeholder-goals)
5. [Further UX Design: ](#ux-design-decisions)
    1. [Skeleton - Wireframes; ](#wireframes)
    2. [Surface - Fonts; ](#fonts-chosen)
    3. [Surface - Colours](#colour-scheme)
    4. [Surface - Imagery](#design-images)
6. [Agile Methology: ](#agile)
    1. [Project setup](#project)
    2. [Designing an Issue Template](#issue-template)
    3. [Creating project issues](#project-issues)
    4. [EPICs ](#epics)
    5. [MoSCoW Prioritisation;](#moscow-prioritisation)
    6. [Level of Effort estimation - Story Points](#story-points)
    7. [Project Milestones](#milestones)
    8. [Project Sprints](#sprints-and-iterations)
    9. [Issue Lifecycle](#issue-lifecycle)
    10. [Project tabular view](#tabular-projects-view)
    11. [Kanban board](#kanban-board)
    12. [Observations and learnings](#agile-observations-and-learnings)    
7. [Features](#features)
    1. [Included](#features-in-scope)
    2. [Future Development](#features-left-to-implement)
8. [Technology](#technologies)
    1. [Languages](#langugages)
    2. [Frameworks and Tools](#frameworks--tools)
9. [Validation](#validation)
    1. [HTML Validation](#html-validation)
    2. [CSS Validation](#css-validation)
    3. [Javascript Validation](#javascript-validation)
    4. [Accessibility](#accessibility)
    5. [Performance](#performance)
    6. [Multi-device Testing](#multi-device-testing)
    7. [Multi-browser Testing](#multi-browser-testing)
    8. [Testing user stories](#testing-user-stories)
    9. [Unfixed Bugs](#unfixed-bugs)
10. [Accessibility](#accessibility)
11. [Performance](#performance)
12. [Deployment](#deployment)
13. [Credits](#credits)
    1. [Content](#content)
    2. [Media](#media)
    3. [Code](#code)
    4. [References](#references)
    5. [Acknowledgements](#acknowledgements)

## About
---------
Jeweller is a system which is designed for a real-life retail Jewellery business.  This business built a first website 4 years ago (https://goldmark.ie/), but it was not integrated with the retail business or everyday processes, and was not successfully implemented.  It remains in use as a 'shop window' only but is not maintained, with most products showing as 'out of stock', and online orders discouraged.  The business owners are, however, quite active on facebook and tend to use that channel for advertising and organic marketing - marketing to existing customers and friends of the business.  Facebook is used to  showcase custom-made products, and to promote/suggest time-based purchases, e.g. Valentines Day, Communion, Mothers Day, Confirmation, Fathers Day, monthly birth-stone, Christmas.   The business operates in a medium sized town in the south-east of Ireland, and currently makes all sales in-person, relying on the customer to physically visit.  (Often this will start with an enquiry phonecall) .  There are two competing jewellers in close proximity.

The Jeweller business offers four lines of business:
* retail jewellery, brand-name watches, zippo lighters, accessories - off the shelf;
* customised retail jewellery, e.g. engraved lighters or hip flasks.
* retail jewellery - custom-made (this process generally begins with the customer making an enquiry as to a particular design, or wishing to re-use and re-fashion their own gold jewellery items);
* repairs and watch batteries (customer repairs and trade repairs);

As a family-owned and -operated business the unique selling points are:
* well established, multi-generational business (the owners are the 3rd generation to operate jewellery businesses in Ireland, and have been in operation in their current location for approx 35 years);
* skilled craftsmanship, with the use of high tech equipment (e.g. laser welder) which means that challenging repair jobs can be undertaken;
* quick turnaround time for repairs;
* personable approach, investment in long term, personal, first-name-terms relationship with customers, which leads to significant repeat business;
* celtic and heraldic jewellery creation;
* affordable pricing and payment flexibility e.g. lay-away schemes allowing customer to pay initial deposit & staged payments before obtaining the product.  

The challenges of the current business model (which may be partly addressed with a fresh ecommerce strategy) are:
* Existing customer base is aging, need to reach a newer generation & persuade them of the value offering
* Competition from online retailers (the 'low cost' model)
* Retail business is staff-heavy and takes staff away from more profitable back-room tasks
* Need to differentiate vs. local jewellers
* Retailer not willing unwilling to stock certain popular brand names, due to restrictive to merchandising constraints 

**This Jeweller e-commerce offering** is:
* a website
* proposed integration with the Jeweller's business processes
* an integrated marketing strategy with example content 

### Responsiveness
The site is built, with the help of Bootstrap 5, to be fully responsive so it can be used on a range of devices.

<details><summary>Responsive Mockup</summary>
<img src="./jeweller/docs/readme_images/val-responsive.png">
</details>

### Live webpage link
https://jeweller-bd1caeb15bbd.herokuapp.com/

## Project Goals
----------------
1. To provide a website and associated marketing materials
2. Which aligns with the jewellers current business processes
3. And provides reach into new market segments
4. Which uses the capabilities of Django python, HTML, CSS and Javascript.
5. And is accessible, responsive and relevant.
  
### UX Design Strategy
Good navigation is key  Good quality imagery for product photos.  Flexible site with good search and filter capabilities.
User feedback form to handle/encourage enquiries

### UX Design Strategy Analysis of Competitors
The following websites were reviewed as part of an assessment of features:
Bramleys
Douglas Jewellers
Simone XXXXX Australian jeweller.
Generally the websites in this space tend to be strong on imagery and imagination, but perhaps somewhat lacking in personality and features.  The website Simone XXXX australian jeweller stands out as having some very interesting and relatable features such as an asynchronous 'chatbot' approach to FAQ.

### UX Design Strategy Target Audience
Target audience is people who might not otherwise make it across the threshold
a. Individuals with an interest in Celtic jewellery
b. Individual with an interest in personalised jewellery (e.g engraved)
c. Individuals who have a unique or unusual requirement e.g. fainne badges
d. Individuals who seek unique custom-made jewellery to be made with jeweller-provided stones and metals
e. Individuals who seek unique custom-made jewellery to be re-made from their existing jewellery items
f. Local people who are not aware of the services on offer (particularly repairs)
g. Who have some purchasing power
h. Who are based in Ireland
i. And possibly have a connection to Carlow Town

## UX Design Scope
----------------
### UX Design Scope - Geographical & shipping constraints:
Currently interested in orders to be shipped within Ireland only.
Due to concerns about fraud, shipping will be done to verified customers only.  
If the customer is not known to the shop, their first online order must be collected in-person.
Thereafter, shipping is to customers home address only (credit card address).

### UX Design Scope - Data
Initial themes loaded 

### UX Design Scope - User Requirements and Expectations
<ul>MVP Requirements:
<li>Must be intuitive to use</li>
<li>Must be easy to learn</li>
<li>Good for first time or returning users</li>
<li>Accessible - no ad display & no paywall</li>
<li>Easy search & filter</li>
<li>Images quick to load</li>
<li> order processing straightforward and intuitive</li>
</ul>
<br>
<ul>Requirements - Desirable:
<li>Should have administrator portal which allow for:</li>
<li>  creation and maintenance of product catgories</li>
<li>  easy creation and maintenance of products, with defaults coming from parent category</li>
<li> easy upload of product images</li>
<li> a means of integrating blogs</li>
<li> a means of identifying date-based promotions</li>
  and displayed will be based on ROI (Republic of Ireland) datasets

## User Goals/ User Stories
----------------
Written in the format 'As a **role** I want to **action** to achieve **desired outcome**    
### Site owner/moderator Goals
* SO_01 As site owner I want to provide a platform where users can directly access useful resources to help with real-life financial decision making
* SO_02 As site owner I want to largely (but not entirely) re-use/ connect to information from authoritative sources 
* SO_03 As site owner I want to avoid connecting to information which is opinion- rather than fact-based (ie perhaps from a less authoritative source) or at least highlight that the source is less authorative, or offered by a biased source.
* SO_04 As site owner I want to provide straightforward, intuitive, consistent website navigation, (using graphical navigation where possible, even where the destination leads to text-based informataion)
* SO_05 As site owner I want to allow users to 'chop and dice' complex information into small chunks 
* SO_06 As site owner I want to provide a website, which meets current programming, performance and accessibility standards (html, css, javascript, responsive, accessibility, performance)
* SO_07 As site owner I want to provide an opportunity for the user to provide feedback, including reporting issues, or suggesting improvements to the Financial Planner site
* SO-08 As site owner I want to acknowledge to the user that their feedback has been received
* SO-09 As site owner I would like to store a database of content to include url links, 
* SO-10 As site owner, I would like to have the capability to organise the content by lifestage, theme, and other criteria (possibly hierarchical groupings, hashtags) to allow cross referncing of user needs to content 
* SO_11 As site owner, I would like to encourague users to engage with each article's content, by providing suggested actions and next steps for the user to take 
* SO_12 As site owner, I would like to provide a personal database where users can store their own actions and record their progress in following the steps
* SO_14 As site owner, I would like to make the content of the database shareable and reusable to others (perhaps subject to signing a re-use agreement) by providing an API to the published database

### First-time User Goals
* FTU_01 As a first time user I want to access relevant information to increase my financial understanding/literacy on a specific topic
* FTU_02 As a first-time user I about what this site does, and want to quickly understand this site's relevance to me, so I don't waste my time on useless engagement 
* FTU_03 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 
* FTU_04 As a first time user I would like to understand the acountability and trustability of information presented on the site - maybe via an 
about page which clearly identifies information souces, information gathering/harvesting processes including moderation (flowchart would be good here).
* FTU_05  As a first-time user I would like to undertand the role of user feedback and user reviews 'X users found this useful or relevant',
* FTU_06 As a first-time user I want clear, timely and unambiguous feedback and interaction
* FTU_07 As a first-time user I expect links and functions that work as expected
* FTU_08 (FUTURE) As a first time user I would like to understand the part I can play in contributing to the body of knowledge


### Returning User Goals
* RU_01 As a returning user I want to mark information I find useful so I can quickly access it again (favourites)
* RU_02 As a returning user I want to create a user profile so that I can personalise my site experience (profile image, bookmarks, actions)
* RU_03 As a returning user want to build my knowledge in certain areas
* RU_04 As a returning user I want to build the body of knowledge for other users (by adding credibility ratings).

### Other stakeholder Goals
* OT_01 As an educator I would like to be able to provide mied-media content and task-related elements such as worksheets  
* OT_02 As The Department of Finance Ireland I want to use this site towards achieving financial literaccy objectives


## UX Design Decisions
----------------

### Wireframes
<details><summary>Landing Page - Articles</summary>
<img src="./django_financial_planner/docs/readme_images/wireframe-01-articles.png">
</details>

<details><summary>Lifestage Planner - themed access to Articles</summary>
<img src="./django_financial_planner/docs/readme_images/wireframe-02-themed-articles.png">
</details>

<details><summary>Article detail - with suggested actions</summary>
<img src="./django_financial_planner/docs/readme_images/wireframe-03-article-detail.png">
</details>

<details><summary>My Planner - personalised user profile/action tracker</summary>
<img src="./django_financial_planner/docs/readme_images/wireframe-04-my-planner.png">
</details>


<details><summary>About/ Feedback page</summary>
<img src="./django_financial_planner/docs/readme_images/wireframe-05-about-feedback.png">
</details>
  
### Fonts Chosen
The website itself is designed to be fairly unobtrusive.  Article fonts were somewhat limited with the standard range of Summernote (Article content creator) fonts, the best of the options seemed to be Arial 16.

### Colour Scheme 
Again, designed to be fairly unobtrusive and not to draw attention to the background.  The articles themselves contain a colourful image and content may include images.  A green background colour and a default green-money logo have been used where possible on the site.

### Design Images

### Design Images - Icons and Symbols

Consistent icons and symbols are used throughout the site, and in multiple contexts - e.g. Certain icons for likes, bookmarks, tasks, and responses (comments) appear in both a user and an article context.  These are descibed more fully within the features section.

## Agile
An Agile approach was followed in plannning this project.  This is somewhat in contrast to the developer's well-practised 'waterfall' habits and presented both a challenge and an opportunity to think in a different way about deliverables and incremental delivery.
It was helpful that the developer participated in a hackathon during Sept 2023, and had an opportunity to observe experienced Agile developers, and their use of Github issue tracking in a team environment.
This led to a much clearer understanding of User story and task breakdown, as well as how github can be tailored  to add value, rather than overhead(!), to programming work.
* One precept which was difficult to master was respecting the timeboxing of each iteration.  Attempts to 'just finish' a task by extending the iteration by a day or two, needed to be curbed.  Instead, I had to (will have to) train myself to end the sprint, then assess which work had been completed or not.
* Story points present another challenge.  A very natural interpretation of story points is to assign them a time value (rather than an 'effort' value).  So, at the outset, the most natural approach felt like assigning each task an estimated duration, and reflecting on story points as hours.  This allowed me to capacity plan the first couple of sprints/ iterations based on the time I had available..... I await to see if I will continue this as the project progresses, or whether I move to a more fluid interpretation of SPs.
* However with the magic law of time (better check what magic law this is) creative tasks in which I am fully engaged make the time fly, meaning I can spend quite a bit of elapsed time but without feeling the strain, whereas less desirable tasks cause time to drag!  <- how does this reflect story points?
* Agile representation using github tools

   
### Project
A github project was created within the Financial_Planner repo.  At a high level the project details are very simple really just a name and description.
<details><summary>GitHub Project Setup</summary>
<img src="./django_financial_planner/docs/readme_images/agile-overview-of-project2.png">
</details>


### Issue Template
<details><summary>Issue template - User Story</summary>
<img src="./django_financial_planner/docs/readme_images/agile-issues-template.png">
</details>
    
At the outset, an issue template was created specifically for user stories.  This holds 5 sections:  
* EPIC:  The parent functional theme for this user story
* A statement of what is to be achieved in the format 'As a **role** I want to **action** to achieve **goal**'.
* Assumptions made when creating this isssue (e.g. pre-requisites)
* Acceptance Criteria: List of conditions to demonstrate the issue has been satisfied/resolved
* Tasks:  Checkbox-marked list of tasks to address this user story.

Mid-way through the project, I created a template to capture project bugs to facilitate separate tracking/reporting.
I found this useful for 'larger' bugs although I maintained an issue logging spreadsheet for the project, and logged almost 70 issues in the 6 or so weeks of development.


### Project Issues
Issues were created to track planned end-to-end work in Financial_Planner, using the issue template for consistent appearance and content.   
Financial_Planner project scope includes UX design tasks, agile project setup, development tasks, documentation,  and testing.
<details><summary>Example issue - user story</summary>
<img src="./django_financial_planner/docs/readme_images/agile-issue-example-user-story.png">
</details>

Some of the issues created were in fact tasks, which underpinned several user stories:
<details><summary>Example issue - task</summary>
<img src="./django_financial_planner/docs/readme_images/agile-issue-example-task.png">
</details>


### EPICs
An epic in agile is a large body of work that can be broken down into a number of smaller stories, which are represented as github Issues.
The Financial_Planner project uses custom fields to hold the epic name, some initial high-level epics:  Agile, UX, Docs, MVP.
For clarity EPIC is also listed at the top of each issue.
<details><summary>EPICs</summary>
<img src="./django_financial_planner/docs/readme_images/agile-epics.png">
</details>


### MoSCoW prioritisation
For prioritising user stories and known tasks, I assigned a label to each issue, one of:
* Must-have
* Should-have
* Could-have (or nice-to-have)
* Won't have (perhaps its a never, or perhaps this just means 'not at this release')
To make selection easier (ensure that these appeared at top of label list in the order above) I preceded each label with a number as shown:
<details><summary>MoSCow labels</summary>
<img src="./django_financial_planner/docs/readme_images/agile-issues-moscow-prioritization.png">
</details>


### Story Points
Story points are intended as a 'level of required effort' measure.  I used a custom issue category field to represent these. 
While at the beginning it was easiest to think of story points in terms of 'hours', as the sprints passed it became easier to assess relative to work already completed.
An observation would be that interpreting story points as 'hours' is somewhat one-dimensional, as sometimes the elapsed hours can be greater or lesser depending on mood, state of flow etc.


### Milestones
While this is a relatively short project (developed over 2 months duration), there was sufficient opportunity to set milestones for MVP (mostly consisting of must-have issues) and releases.
The use of MVP milestone encouraged a 'deploy-early' mindset whereby the software could be delivered incrementally, with successive releases building on proven, working software.  
When creating the milestone a due date is needed, initially I set a due date of 3 weeks prior to deadline for MVP, with additional release dates scheduled up to the project deadline.

This approach ensured, it would be possible to deliver a working, functional system, even if difficulties were encountered with implementing some of the 'could-have' features..
<details><summary>Milestones</summary>
<img src="./django_financial_planner/docs/readme_images/agile-milestones.png">
</details>

### Sprints and Iterations
In Agile methodology, effort is timeboxed into Srints, with a kickoff at the start of each Sprint time period, in which items from the product backlog are made ready for work (groomed) by ensuring all the details are completed on the user-story/issue card (task details, acceptance criteria, priority, dependencies, Story Point estimate ) before a developer starts working on it.  At the end of a sprint a retrospective should be undertaken to determine what worked well or not during that sprint.
For Financial_Planner a time-period of weekly sprints was chosen.  Loosely (given that the developer consisted of a one-person team), the sprint ran from Monday-Sunday inclusive, and the aim was to complete certain agreed user stories during a particular sprint.

<details><summary>Sprints/ github Iterations</summary>
<img src="./django_financial_planner/docs/readme_images/agile-sprint-iteration-weekly.png">
</details>

Initially when performing the design tasks (effectively the first four sprints), the timeboxing aspects were not fully respected.
However from sprint5 onwards (the first programming sprint), it became easier to decide clearly what was to be included at the outset of each sprint, and to pull specific issues from the backlog and ensure that they were progressed during the planned sprint. 
I started doing formal sprint reviews with burndown charts, at end of:
[Sprint 5 retrospective]([Issue #24](https://github.com/DeeMcCart/CI_PP4_Financial_Planner/issues/24 target="_blank") )

[Sprint 6 retrospective]([Issue #33](https://github.com/DeeMcCart/CI_PP4_Financial_Planner/issues/33 target="_blank") )

[Sprint 7 retrospective]([Issue #35](https://github.com/DeeMcCart/CI_PP4_Financial_Planner/issues/35 target="_blank") )

[Sprint 8 retrospective]([Issue #47](https://github.com/DeeMcCart/CI_PP4_Financial_Planner/issues/47 target="_blank") )

As each weekly sprint progressed, I became more fluent with the insights/ burndown charts and started to develop to include actual time logged, a useful metric


### Issue Lifeycle
An issue is set to progress through a number of stages, each represented by a status during its lifecycle.  
Issues progressed through:
* Backlog 
* To-do
* In-progress
* Review
* Done


### Tabular Projects View
The tabular view of projects was very useful at the backlog grooming stage, as it shows open issues, and gives easy visiblity of associated fields, e.g. story points, epic, assigned sprint, etc 
<details><summary>Projects - Tabular view</summary>
<img src="./django_financial_planner/docs/readme_images/agile-overview-of-project.png">
</details>

<details><summary>Projects - Tabular view2</summary>
<img src="./django_financial_planner/docs/readme_images/agile-issues-tabular-view.png">
</details>

    
### Kanban board
Within a sprint, the kanban board provides invaluable visual tracking.  
In the Financial_Planner kanban board, issues progress from leftmost column (backlog) to rightmost (done)
Note that each column holds a descriptor to tell you what is happening to issues within the column.
<details><summary>Projects - Kanban (simple)</summary>
<img src="./django_financial_planner/docs/readme_images/agile-issues-kanban-view.png">
</details>

An improved kanban view (developed mid-way through the project) is shown here, note that this shows:
* the number of issues at each kanban board state (e.g. highlighted in blue for InProgress column)
* The storypoints for each individual issue, as well as the total storypoints at each lifecycle status (e.g. highlighted in green for 'Todo' column)
* The EPIC associated with each issue (e.g. highlighted in pink within the 'Done' column)

![Projects - Rich Kanban board](./django_financial_planner/docs/readme_images/agile-issues-kanban-view-sp-epic-num-issues-per-col.png?raw=true "Improved kanban board with lots of information")

 
### Agile Observations and learnings
* Observation from hackathon - short user story names are best for visibility and tracking
* Observation from hackathon - a user story is generally a fairly big block with a number of subtasks.  It is not advisable to have an entire user story which is longer than a sprint, as it will be carried forward in the 'to do' or 'in progress' bucket without clear visibility.  Therefore likely to try breaking a complex user story into sub-stories/tasks.  Both the user story and the sub tasks will be listed as issues, the user story will remain in the 'to do' bucket after grooming, and its tasks will be ticked off when their individual issues are completed.  The individual issues will move through the kanban board lifecycle of backlog -> to do -> in progress -> review -> done.  The 'parent' user story will remain at 'to do' (or possibly 'in progress'???)
* Observation from hackathon - when merging of PR (pull requests) was performed in a distributed development environment, it was possible to link the PR to a kanban issue, and to automatically update the issue status based on the PR.   I would be interested in exploring how ths might be done for a solo developr (possibly workflows?)
* Observation - if I reference the issue # on a commit (but must be in the format #8 ) then I can hyperlink from that commit message back to the relevant user story or issue.
* Use of EPIC as a label rather than as an issue - this was an early decision, although when reviewing our cohort leader Alan Bushell's PP4 project, he showed how he had used Issues within Github to represent EPICS.  This seemed to work really well as it was possible to demonstrate a hierarchy of EPIC -> issues by including a link to the sub-issues within the EPIC 'issue' body.  Thus it was possible to click on the issues within the EPIC, check their status, then return to the EPIC.
At the time of seeing this I had already committed to using labels to represent EPICs, so I stayed with my original approach just to see how it would work in practice.
* Use of a public project repo - I made the repo public early on, as I had assumed this was needed for assessment.  And about half way through I was surprised to see some comments on my tasks from another (unknown) github user offering assistance with development - kind of like an open source approach.  So they had commented on a couple of tasks.  I kept the repo public, but changed the settings so that only users who had previously committed to the repo could comment, and I blocked that particular user from the workspace....

## Features 
Implemented features are fully documented in the Features readme, located at  

### Features in Scope 

<a href="https://github.com/DeeMcCart/CI_PP4_Financial_Planner/blob/main/README_Features.md" target="_blank">Site features</a>

It was helpful to create this as a separate document, as it is also offered to users as a 'how to' guide.

### Implementation Decisions
This project was somewhat unusual for me as I followed the Agile principle of not defining every feature fully at the start of a 8-week project process.  Instead, the project evolved and took its own shape over the duration.  I followed a principle of incremental delivery, deployed early and established the core structures pretty much as per the walkthrough training given.
<br>  
Some of the site ideas and features needed only really became clear as I played with the site as it was delivered, and experienced frustration or spotted opportunites or elements that were worth adding. So the site grew organically as time went on.
<br>
And it would still be growing organically if I didn't have a project dealine to submit (sometimes deadlines are really useful!!!)

### Features Left to Implement

#### F18 Write a custom app for Admin Console (FUTURE)
The FinancialPlanner site as delivered is a good base site with strong core functionality in the areas of content and task management. It has a decent front-end and is depends strongly on a standard Django Admin console in the backend.  However, as the site has incrementally developed, the database model complexity has increase, so there are a number of tables which need to be manually synchrnised, for example articles vs structured search tags, these are maintained separately and require some overhead to ensure they remain well-designed and consistent.
So this site would definitely benefit from a well-designed admin console to simplify the database maintanance overhead

#### F19 Content Creation (ONGOING & FUTURE)
Development of the site has required considerable programming effort however to really make it flourish, well-designed, appropriate content is needed.  There is huge scope for worksheets, budgeting lists, and many other tools to be created and made available to users.  This is where the real site benefit lies, in practical, relevant content that is easily understood and convertible into actionable tasks.

#### F20 Gamification (DEFINITELY FUTURE)
One of the original hopes for this site was to include a 'Game of Life' concept whereby a user could start with a notional financial health rating then take decisions and see the financial impact.  This is effectively a financial modelling exercise, the concept of a 'game' makes it less threatening to users, whereas, it could in fact act as a simulation providing 'what if' financial implications of life decisions.

#### F21 Structured/Lifestage search (NEAR-FUTURE)
The use of the structured article tags to provide a lifestage search feature has been designed and is operational in the backend, but doesnt yet have a front end implementation. This is a key feature as it would allow much more granular content filtering and greatly assist users by filtering down to just articles aligned with the user's needs e.g. 'I want to.... get a mortgage', 'I want to.... move to Ireland', 'I want to.... plan for later life' 

#### F22 UX and Integration features
Would like a 'share' button on articles and the ability to connect to whatsapp and other social media portals.
Would like to be able to send email notification for password reminders.
Would like to improve appearance of task and response windows, they are functional now but could be more beautiful.

#### Other features to be identified via target-user interaction
There are lots of other features which could be useful.  The version of FinancialPlanner delivered today is really a proof-of-concept and ideally it would now be exposed to a wider group of potential users, and based on their feedback and real-life needs, a development road map coud be established.  In the absence of an app to show, it has been difficult to have the 'what would you like in a financial literacy app?' discussion with potential users, but the FinancialPlanner app as-is is fine for demo and discussion purposes.
I would hope to develop FinancialPlanner further as a commercial app.  
               
## Technologies

### Langugages
- HTML 
- CSS
- Javascript
- Python
- Django (initial v 3, now V4+)
- Bootrap (V5)

### Frameworks & Tools
* Github:  used to maintain the code repository, and for some readme edits and commits
* Git
* Gitpod:  used for editing and for tracking code commits back to Github
* Balsamiq:  used for wireframing
* Lucidchart: used for database diagramming
* Canva: used to create some infographic content
* Leonardo AI: used to create some of the site images

### Python Libraries
The following additional python libraries were used:


### Third-Party Libraries



## Validation 

### HTML Validation 
- HTML
HTML validation was performed for the various site pages as follows:  Render the page via the app, right click on the page contents and take option to copy (rendered) source.  Paste this into a file and subject that file to the W3C validator.  

  - All errors returned from the validator were pursued and resolved.  Examples are shown below:
 
  on the index html pages when checked in the W3C validator:

![W3C Validator - index page](./django_financial_planner/docs/readme_images/validation-w3c-index-html.png?raw=true "W3C validator (index page)")


![W3C validator - my_planner page](./django_financial_planner/docs/readme_images/validation-w3c-myplanner-html.png?raw=true "W3C validator (my planner page)")

![W3C validator - my_actions page](./django_financial_planner/docs/readme_images/validation-w3c-myactions-html.png?raw=true "W3C validator (my actions page)") 

![W3C validator - my_user page](./django_financial_planner/docs/readme_images/validation-w3c-myuser-html.png?raw=true "W3C validator (my actions page)") 

### CSS Validation

No errors returned when passing through the official Jigsaw validator.  

- ![(Jigaw) CSS Validator)](./django_financial_planner/docs/readme_images/val-css.png?raw=true "CSS validator") 


### Performance
Performance for all pages was tested using the Lighthouse tool within Google Chrome.  Performance was at 98% for the index page (intro modal).


![Performance - Lighthouse - index](./django_financial_planner/docs/readme_images/validation-lighthouse-performance-index-html1.png?raw=true "Lighthouse - index page") 


![Performance - article detail](./django_financial_planner/docs/readme_images/validation-lighthouse-performance-article-detail-html.png?raw=true "Lighthouse - index page") 


### Device Testing
The website was tested on the following devices:
* HP laptop & associated widescreen monitor
* Samsung Galaxy S10 tablet
* Motorola G(7) android phone
* Lenovo IdeaPad Flex3 (mini laptop)

### Multi-browser Testing
The website was tested on the following browsers:
* Google Chrome v112.0.5615.138 (HP laptop)
* Google Chrome v112.0.5615.136 (Samsung Galaxy tablet)
* Mozilla Firefox v112.1.0 (Motorola g(7) phone)

### Testing Features
![Feature testing page1](./django_financial_planner/docs/readme_images/val-feature-p1.png?raw=true "Feature testing page1") 

![Feature testing page2](./django_financial_planner/docs/readme_images/val-feature-p2.png?raw=true "Feature testing page2") 

![Feature testing page3](./django_financial_planner/docs/readme_images/val-feature-p3.png?raw=true "Feature testing page3") 


### Bugs and issues
Almost 70 issues were recorded, I used an excel spreadhseet to keep track.  

The structure of the log is shown here:

![Feature testing page3](./django_financial_planner/docs/readme_images/val-issuelog.png?raw=true "Feature testing page3") 

There are a number of smaller responsiveness issues still open at the time of writing (icon alignment on mobile phone)


## Deployment
<br>
* The site architecture requires git, Cloudinary, ElephantSQL to support PostGres database, Heroku and is therefore more complex.

 The steps to setup are as follows:
 
 #### Install the Django environment in a workspace created with the CI template:

- pip3 install 'django<4'gunicorn (installs Django 3.2)
- pip3 install dj-database-url===0.5.0 psycopg2
- pip3 install dj3-cloudinary-storage
- pip3 install urllib==1.26.15
- pip3 freeze --locaL>requirements.txt
- django-admin startproject django_financial_planner
- python3 manage.py startapp fp_blog (creates new app in project)
- settings.py INSTALLED_APPS = [..'appname'...]
- python3 manage.py migrate (migrate changes)
- python3 manage.py runserver (1st run of server to test)
- settings.py ALLOWED_HOSts = [...'8000-address'..]

##### Create a new external database:

- ElephantSQL - setup a/c if needed
- create a new instance
- Click on created database and copy URL

#### Create the Heroku app:

- login to Heroku
- create a new app
- In settings tab, reveal cofig vars and add newDATABASE_URL = save link

#### Attach the database:

In dev environment root dir add env.py
import os
os.environ['DATABASE_URL']=['pasted URL from elephant']
os.environ['SECRET_KEY']='some key"

Add secret key to Heroku config vars

#### Prepare environment and settings.py file
settings.py:  
if os.path.isfile("env.py"): import env
SECRET_KEY = os.eviron.get(SECRET_KEY)
DATABASES = {'default':dj-database-url,parse(os.environ.get("DATABASE_URL"))}
Save all files and migrate

#### Get our static and media files stored on Cloudinary

Create cloudinary account (if not already done)
Pickup the API config variable from the cloudinary dashboard
env.py:
add os.environ["CLOUDINARY_URL"]="urlpath"

Heroku: add CLOUDINARY_RL to config vars
add DISABLE_COLLECTSTATIC (for testing phase only)

settings.py: Add Cloudinary to installeed apps
STATICFILES_STORAGE = 'cloudinary-storage.storage.staticHashedCloudinaryStorage'
STATICFILES_DIRS
STATIC_ROOT
MEDIA_URL
DEFAULT_FILE_STORAGE
BASEDIR..... TEMPLATES_DIR
TEMPLATES
ALLOWED_HOSTS

create the following root-level folders: media, static, template

Create a procfile (process file)
commit
From Heroku panel, deploy from main & test.

#### Crack on with development
Thereafter you are into building models, forms, templates etc

### Deploy to Heroku
If you wish the site CSS to be picked up by Heroku (it is possible to deploy without this, and the functionality will be loaded to Heroku app & database can be tested  -but the apperance will not be good)
but anyway when you want to check appearance
settings.py
DEBUG = False
Heroku
remove the config var for static files 


#### To re-deploy
Can set automatic redeployment in Heroku, this will refresh the app at every commit - useful for consistency checks

#### To fork the repository:
- Go to the GitHub repository
- Click on Fork button in the upper right hand corner

* To clone the repository:
- Go to the GitHub repository
- Locate the Coe button above the list of files and click it
- Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to you clipboard
- Open Git Bash
- Change the current working directory to the one where you want the cloned directory
- Type git clone and paste the URL from the clipboard($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
- Press Enter to create your local clone


## Credits 
Multiple sources were used in assembling this site.


### Content - Financial Planner
* Inspiration taken from many many sources
* Ref the UX strategy section

### Financial Planner site ethos - authenticity
https://nobsmarketplace.com/blog/how-do-you-know-if-website-authoritative/ offers a definition of an authoritative website as 'a trusted source that offers reliable information to users'
https://nobsmarketplace.com/blog/how-do-you-know-if-website-authoritative/ factors to determine an authoritative website: site domain name/url; value offered to the user; reputable sources (with verifiable credentials); quality of inbound & outbound links; website UX, design & functionality; proven user trust & engagement (e.g. measured by organic comments, likes and shares given by customers/users, as well as the quality of the audience the website has attracted)

### Agile implementation in github
* https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-text-and-number-fields#adding-a-number-field to understand how story points might be represented in GitHub
 
### Code - Financial Planner
Dennis Ivy
Multiple Code Institute PP4 projects used for reference

 
### Acknowledgements
* I would particularly like to thank Alan Bushell, our cohort facilitator who guided us through this partiularly diverse phase of the course, kept us on track with weekly standups, ensured we all stepped into the limelight and provided really useful advice.
* I would like to sincerely thank my mentor, Mo Shami for his kindness, enthusiasm and support throughout.  Mo's ability to absorb the essence of a situation and to communicate a clear path ahead has been invaluable.
* I would also like to thank Derek and my family for their personal support, and for their help with system testing.





![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Deirdre McCarthy,

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.


------


---

Happy coding!

Credits:
uxwing:  for social media icons
font awesome:  for avatar, shopping basket icons
