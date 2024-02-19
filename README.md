# Jeweller 
Developer:  **Deirdre McCarthy**, Feb 2024

Testing the ability to create links that open in a new window:

[Link Text](Link URL) {target="_blank"}

<a href="URL" target="_blank">Text description</a>

<a href=(https://github.com/users/DeeMcCart/projects/5) target="_blank">Kanban Board</a>


[Kanban Board]() {target="_blank"}


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
Jeweller is a system which is designed for a real-life retail Jewellery business.  This business built a first website 4 years ago (https://goldmark.ie/), but it was not integrated with the retail business or everyday processes, and was not successfully implemented.  It remains in use as a 'shop window' for off-the-shelf items, but is not maintained, with most products showing as 'out of stock', and online orders discouraged.  The business owners are, quite active on facebook for (free) advertising and organic marketing - marketing to existing customers and friends of the business.  Facebook is used to  showcase custom-made products, and to prompt time-based purchases, e.g. Valentines Day, Communion, Mothers Day, Confirmation, Fathers Day, monthly birth-stone, Christmas.   The business operates in a medium sized town in the south-east of Ireland, and currently makes all sales in-person, relying on the customer to physically visit.  (Often this will begin with an enquiry phonecall) .  There are two competing jewellers in close proximity.

The Jeweller business offers four lines of business:
* retail jewellery, brand-name watches, zippo lighters, accessories - off the shelf;
* personalised retail jewellery, e.g. engraved lighters or hip flasks.
* retail jewellery - custom-made (this process generally begins with the customer making an enquiry as to a particular design, or wishing to re-use and re-fashion their own gold jewellery items);
* retail services - repairs, watch batteries and valuations;
* trade repairs (on behalf of other jewellery retailers);

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
* Retail business is staff-heavy and takes skilled staff away from more profitable back-room tasks
* Need to differentiate vs. local jewellers
* Shop owner unwilling to stock certain popular brand names, due to restrictive to merchandising constraints 

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
Two local jeweller's websites
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
### First-time User/ Unregistered User
* FTU_01  As a **First-Time User** I want to **quickly understand the site purpose** so I **can decide whether to spend time exploring and discovering the site**
* FTU_02  As a **First-Time User** I want to **easily navigate the site** so I **don't become frustrated and leave**
* FTU_03 As a **First-Time User** I want to **receive feedback at each step on the site** so that I **understand what I am doing, and, if I'm in a multi-step process, I understand how far along I am in the processs**
* FTU_04 As a **First-Time User** I want to **access this site on a device of my choosing (mobile, tablet, laptop, desktop)** so that I can **access by a method and at a time that is convenient and accessible to me**
* FTU_05 As a **First-Time User** I want to **navigate the site without mandatory login** so **I can discover site features before deciding whether to commit to using site**
* FTU_06:  As a **First-Time User** I want to **see a range of products which are offered by the Jeweller, to see pictures, descriptions price (for off-the-shelf items), lead-time for each item** so that I can **make purchase decisions**
* FTU_07:  As a **First-Time User** I want to understand **whether an item is in-stock, made-to-order** and **what are lead times (e.g. available now, lead time 6 weeks for make-to-order, lead time 1 week for casted items)**
* FTU_08:  As a **First-Time User** I want to **search for a product by name or description** to **know if Jeweller sells the item of interest**
* FTU_09:  As a **First-Time User** I want to **filter my product view** to **see only what I'm interested in ** (e.g. particular metals, stones, colours, particular occasions) (Preferably filter by multiple categories)
* FTU_10: As a **First-Time User** I want to **sort my product view by price, date added ....** in order to **see the items most relevant to me**
* FTU_11: As a **First-Time User** I want to **view custom products** in order to **get inspiration for my design idea**
* FTU_12: As a **First-Time User** I would like to be able to **receive prompt on affinity items** in order to **see items that are related to the item I'm interested in (e.g. earrings may have matching necklace or bracelet)**
* FTU_13: As a **First-Time User** I would like to receive suggestions or prompts for particular occasions (which could be date-related e.g. communions, confirmations, mothers day, christmas)
* FTU_14:  As a **First-Time User** I want to be able to **share/like a item I like with a 3rd party (e.g. via whatsapp, fb etc)** so I can **prompt them to buy it (for me!)** <- affinity marketing

* FTU_15: As a **First-Time User** I want to **create a shopping basket of items** in order to **determine price**
* FTU_16: As a **First-Time User** I want to **amend or remove items in my shopping basket** in order to **determine price**
* FTU_17: As a **First-Time User** I want to **convert my shopping basket into a collection order** in order to **purchase items**
* FTU_18: As a **First-Time User** I want to **personalise my order** to **reflect gift messages, special wrapping etc**
* FTU_19: As a **First-Time User** I want to **pay for my order using credit card** to **ensure the purchase is completed**
* FTU_20: As a **First-Time User** I want to **receive an on-screen confirmation of order number** to **ensure the purchase is completed**
* FTU_21: As a **first-Time User** I want to **receive email/text notifying me of my order number and lead time** so I can **plan when to collect**

* FTU_22: As a **First-Time User** I would like to **complete an enquiry form** to **ask a question about products or services**
* FTU_23: As a **First-Time User** I want to **see services offered (repairs, make-to-order items,** to achieve **benefit**
* FTU_24: As a **First-Time User** I want to **browse the Jeweller's blog** to **increase my affinity with this retailer**
* FTU_25: As a **First-Time User** I want to **consult the Jeweller's FAQ** to **understand the retailer's processes for orders, shipping etc**

* FTU_26: As a **First-Time User** I would like to **signup for newsletter** to **increase my affinity with this retailer**
* FTU_27: As a **First-Time User** I would like to **create a profile** to **track my history with this retailer**

* FTU_28 (Future): As a **First-Time User** I would like to  **make an appointment for engagement rings** in order to **elevate a high value buying decision**


### Returning User - Additional Goals
* RU_01 As a **Returning User** I want to **quickly navigate to the Products Page** to **focus on items i'm most intersted in**
* RU_02 As a **Returning User** I want to **filter products by type, type-of-metal, type-of-stone** so I can **see the products I am most interested in**
* RU_03 As a **Returning User** I want to **sort products** by **date added** so i can see what is new on the site
* RU_04 As a **Returning User** I would like **to receive prompts of upcoming celebration days and associated promotions** 
* RU_05 As a **Returning User** I would like to **be prompted with affinity products, based on on what I've previously purchased** so I can **make coordinated buying decisions**
* RU_06 As a **Returning User** I want to **view my order status** so I **know if the order has been shipped**
* RU_07 As a **Returning User** I want to **raise product enquiries on the site** so **I can save time rather than phonning**
* RU_08 As a **Returning User** I would like to **receive an emailed newsletter periodically** so **I am alerted to promotions**
* RU_09 As a **Returning User** I want to **add or update contact details and preferences (email, phone number)** on my profile so **Jeweller can contact me in a way that suits me**
* RU_10 As a **Returning User** I want to **add an image of my choosing to my profile** to **personalise my experience** #45 
* RU_11 As **Returning User** I want to **assign delivery address(es) to my account** to **streamline the ordering process**
* RU_12 As a **Returning User** I would like to **choose a saved delivery address when placing an order** to **streamline the ordering process**
* RU_13 As a **Returning User** I would like to **create Product Reviews and ratings** to **increase interaction with the site and help to guide other purchasers**
 
### Site owner/moderator Goals
* SO_01 As **System Owner** I want to **provide a system that is easy to use** to **encourage users to visit and return to the site** #36 
* SO_02 As **System Owner** I want to **provide responsive web pages** to **encourage users to use the site across multiple devices**
* SO_03 As **System Owner** I want to **include social links** to **increase user engagement with site**
* SO_04 As **System Owner** I want to **use the site as a shop window** to **facilitate unregistered users who will complete purchases in-person**
* SO_05 As **System Owner** I want to **permit guest checkout** to **facilitate unregistered users to complete purchases on the site**
* SO_06 As **System Owner** I want to **track orders raised** to **ensure they progress through the shipping lifecycle**
* SO_07 As **System Owner** I want to **link to an post tracking** to **provide delivery status to customers**
* SO_08 As **System Owner** I want to **create and maintain product catgories** to **benefit**
* SO_09 As **System Owner** I want to **create and maintain items** to **benefit**
* SO_10 As **System Owner** I want to **identify make-to-order/custom products as well as off-the-shelf** products to **advertise both business streams**
* SO_11 As **System Owner** I want to **create and maintain item affinities** to **benefit**
* SO_12 As **System Owner** I want to **create and maintain time-based marketing promotions** to **benefit**
* SO_13 As **System Owner** I want to **link products product categories to marketing promotions** to **benefit**
* SO_14 As **System Owner** I want to **provide a robust payment interface** so as to **maintain trust and integrity and minimse payment queries**

* SO_XX As site owner I want to showcase my Jewellery business professionally and align with my business values and processes
* SO_XX As site owner I want to provide straightforward, intuitive, consistent website navigation, (using graphical navigation where possible, even where the destination leads to text-based informataion)
* SO_XX As site owner I want to provide a website, which meets current programming, performance and accessibility standards (html, css, javascript, responsive, accessibility, performance)
* SO_XX As site owner I want to provide an opportunity for the user to provide feedback, including reporting issues, or suggesting improvements to the Financial Planner site
* SO-XX As site owner I want to acknowledge to the user that their feedback has been received

  
### Other stakeholder Goals
* OT_01
* 

## UX Design Decisions
----------------

### Wireframes
<details><summary>Landing Page, search & filter functionality </summary>
<img src="./jeweller/docs/readme_images/wireframe-01.png">
</details>

<details><summary>Create a basket</summary>
<img src="./jeweller/docs/readme_images/wireframe-02-basket.png">
</details>

<details><summary>Checkout & additional services</summary>
<img src="./jeweller/docs/readme_images/wireframe-03.png">
</details>

<details><summary>Checkout - address page/action tracker</summary>
<img src="./jeweller/docs/readme_images/wireframe-04-checkout-address.png">
</details>

<details><summary>Checkout - payment page/action tracker</summary>
<img src="./jeweller/docs/readme_images/wireframe-05-checkout-payment.png">
</details>

<details><summary>About/ Feedback page</summary>
<img src="./jeweller/docs/readme_images/wireframe-06-about-feedback.png">
</details>
  
### Fonts Chosen
(To be completed)

### Colour Scheme 
(To be completed) 

### Design Images
(To be completed)

### Design Images - Icons and Symbols
(To be completed)

## Agile
An Agile approach was followed in plannning this project.  Github Issues and Projects were used to track project work as follows:
* Sprints - The project was organised into 5 one-week sprints/iterations Sprint1..Sprint5.
* EPICS - created to track the various streams of work; Stored as github issues (to allow a task hierarchy) AND as Issue custom fields (to allow for analysis in github insights).  Typically include quite a few sub-issues.  
* 6-7 EPICs created for this proect
* Issues - created to represent items of work.  Issues = User Stories are apply a template, which requires a title, statement in the form of As a **role** I want to **action** in order to **benefit**, Pre-requisites and Tasks.
* Gitpod commit messages can reference #XX, this links to issue XX.  
* Github allows multi-media comments per issue,  used for screenprint **proofs** of tsk completion. 
* YY User Story/Task issues were created for this project.
* Bugs - project issues were used to track bugs, an individual template was created for bug data capture.
* Kanban boards - 4 status buckets - backlog, in-progress, review, done.  
* Labels - Used to track MoSCoW prioritisation
* Project fields: Prioritities P0 = top triority, P1, P2
* Project fields: T-shirt Sizing used when grooming backlog at end each sprint
* Project fields: Estimated Story Points (time); actual SPs - used for end-of-spring analysis   
The entire approach was covered under the EPIC 'Agile' and can be seen under this link: https://github.com/DeeMcCart/CI_PP5_Jeweller/issues/10

### Following an Agile process during development:
* Timeboxing each Sprint is challenge.  Attempts to 'just finish' a task by extending the iteration by a day or two, needed to be curbed.  Instead, I had to (will have to) train myself to end the sprint, then assess which work had been completed or not.
* Story points present another challenge.  A very natural interpretation of story points is to assign them a time value (rather than an 'effort' value).  So, at the outset, the most natural approach felt like assigning each task an estimated duration, and reflecting on story points as hours.  This allowed me to capacity plan the first couple of sprints/ iterations based on the time I had available..... I await to see if I will continue this as the project progresses, or whether I move to a more fluid interpretation of SPs.

   
### Project
A github project was created within the Jeweller repo.  At a high level the project details are very simple really just a name and description.
<details><summary>GitHub Project Setup</summary>
<img src="./jeweller/docs/readme_images/agile-overview-of-project.png">
</details>


### Issue Template
<details><summary>Issue template - User Story</summary>
<img src="./jeweller/docs/readme_images/agile-issues-template.png">
</details>
    
At the outset, an issue template was created specifically for user stories.  This holds 5 sections:  
* EPIC:  The parent functional theme for this user story.  
* A statement of what is to be achieved in the format 'As a **role** I want to **action** to achieve **goal**'.
* Assumptions made when creating this isssue (e.g. pre-requisites)
* Acceptance Criteria: List of conditions to demonstrate the issue has been satisfied/resolved
* Tasks:  Checkbox-marked list of tasks to address this user story.
* Associated project tracking fields (MoSCoW label, priority, estimated SPs, actual SPs, EPIC, Assigned-to, associated Project & Milestone)

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

### Estimated & Actual Story Points
Story points are intended as a 'level of required effort' measure.  I used a custom issue category field to represent these. 
While at the beginning it was easiest to think of story points in terms of 'hours', as the sprints passed it became easier to assess relative to work already completed.
An observation would be that interpreting story points as 'hours' is somewhat one-dimensional, as sometimes the elapsed hours can be greater or lesser depending on mood, state of flow etc.

### Milestones
Three project milestones were used:
* First deploy (due date = end Sprint1)
* MVP (due date =  end Sprint2)
* Version 1 (due date = end Sprint4)
This'deploy-early' approach meant the software could be delivered incrementally, with successive releases building on proven, working software.  

<details><summary>Milestones</summary>
<img src="./jeweller/docs/readme_images/agile-milestones.png">
</details>

### Sprints and Iterations
In Agile methodology, effort is timeboxed into Srints, with a kickoff at the start of each Sprint time period, in which items from the product backlog are made ready for work (groomed) by ensuring all the details are completed on the user-story/issue card (task details, acceptance criteria, priority, dependencies, Story Point estimate ) before a developer starts working on it.  At the end of a sprint a retrospective should be undertaken to determine what worked well or not during that sprint.
For Jeweller a time-period of weekly sprints was chosen.  Loosely (given that the developer consisted of a one-person team), the sprint ran from Monday-Sunday inclusive, and the aim was to complete certain agreed user stories during a particular sprint.

At the end of each sprint a formal process was followed:
* retrospective
* backlog grooming & prioritisation
* decision as to what is to be included in next Sprint
* readme Updates

I added the last task, readme updates, based on learning from my previous Code Institute PP4 project, where I'd invested so much effort and detail into the Agile record keeping that I faced an impossible task to duplicate the content into READme at project completion.  So the intention is to keep it Agile with small, incremental updates to the Readme, as well as the code!

Burndown charts were maintained over the 5 project sprints.  These can be seen on the:

Sprint1 Retrospective: Issue # https://github.com/DeeMcCart/CI_PP5_Jeweller/issues/12

Sprint2 Retrospective: Issue # https://github.com/DeeMcCart/CI_PP5_Jeweller/issues/38

Sprint3 Retrospective: Issue # https://github.com/DeeMcCart/CI_PP5_Jeweller/issues/54

Sprint4 Retrospective: Issue # https://github.com/DeeMcCart/CI_PP5_Jeweller/issues/65

Sprint5 Retrospective: Issue #

The insights/ burndown charts were useful to track the actual time logged, a useful metric


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
<img src="./jeweller/docs/readme_images/agile-overview-of-project.png">
</details>

<details><summary>Projects - Tabular view2</summary>
<img src="./jeweller/docs/readme_images/agile-issues-tabular-view.png">
</details>


### Commit Messages
The XXXX convention was adopted this time around for commit messsages, as prviously submitted projects have highlighted small inconsistencies.
Where possible the Kanban issue # is referenced, this links the commit message to the issue on the Kanban board.
    
### Kanban board
Within a sprint, the kanban board provides invaluable visual tracking.  
In the Jeweller kanban board, issues progress from leftmost column (backlog) to rightmost (done)
Note that each column holds a descriptor to tell you what is happening to issues within the column.
<details><summary>Projects - Kanban (simple)</summary>
<img src="./jeweller/docs/readme_images/agile-issues-kanban-view.png">
</details>

Two main Kanban views were used, one for EPICs only, and one for Issues.  See:
* the number of issues at each kanban board state (e.g. highlighted in blue for InProgress column)
* The storypoints for each individual issue, as well as the total storypoints at each lifecycle status (e.g. highlighted in green for 'Todo' column)
* The EPIC associated with each issue (e.g. highlighted in pink within the 'Done' column)

![Projects - Rich Kanban board](./jeweller/docs/readme_images/agile-issues-kanban-view-sp-epic-num-issues-per-col.png?raw=true "Improved kanban board with lots of information")

Viewing by EPIC was useful for an overall view of the project: https://github.com/users/DeeMcCart/projects/5/views/7

Each EPIC contains a drill down into its 'child tasks', e.g. https://github.com/DeeMcCart/CI_PP5_Jeweller/issues/16

Example 'child' task: https://github.com/DeeMcCart/CI_PP5_Jeweller/issues/17

 
### Agile Observations and learnings
* Improvement from PP4 in use of EPICs defined as Issues, which allows a hierarchy of issues to be built
* All user stories are assigned a code e.g. RU_01 is first Returning User story, these are used with an abbreviated title to keep the Kanban board neat.
* To avoid extra documentation work (as I found this quite time consuming in PP4), hyperlinks are used where possible, e.g. on commit message to link to relevant Github Issue. 
* Improvement from PP4 by defining each EPIC as a parent Issue to represent hierarchy (inspired by our cohort leader Alan Bushell),  it was possible to demonstrate a hierarchy of EPIC -> issues by including a link to the sub-issues within the EPIC 'issue' body.  Thus it was possible to click on the issues within the EPIC, check their status, then return to the EPIC.
* While it felt like a bit of duplication, I found on the 'Github Insights' bar charts for sprint retrospectives, the EPIC needed to be defined as a project field to become eligible for chart breakdown & grouping.
* Labels were well used, 'EPIC' Issues were assigned label 'EPIC' where other issues were given a MoSCoW (01_MustHave 02_ShouldHave, 03_CouldHave, 04_WontHave).  Identifing the EPICs with a separate label allowed them to be excluded from the main KanBan board and moved to a separate board.
* This project is quite comprehensive and contains a LOT of user stories!!!  In practice, as part of each end-of-sprint ceremony, I created Issues for the user stories to be done in that sprint.  That helped as it just meant the KanBan board didnt become overwhelming.
  
## Features 
The site includes over 20 features, these are cross-referenced to the user stories as per the screen captures below:

### F01 LOGON	
### F02 SECURITY	
There are currently 4 levels of access to the Financial Planner App.  
Permissions are granted to database objects as follows:

N = No Acceess
C = Create
R = Read
U = Update
D = Delete
| User Type            | Description              | UserID                                         | User Profile                                | Article | Article Approval | Article Like | Article Bookmark | Article Task | Article Comment |  Comment Approval | Personal Task |
| -------------------- | ------------------------ | ---------------------------------------------- | ------------------------------------------- | ------- | ---------------- | ------------ | ---------------- | ------------ | --------------- | ----------------- | ------------- |
| **First Time User**      | Never registered on site | none                                           | N - link disabled                           | R       | N                | N            | N                | R            | R               | N                 | N             |
| **Registering user**     |                          |  Creates allauth 'User' account by registering | C (by adding profile photo once registered) | Read    | N                | CRUD         | CRUD             | CRUD         | CR              | N                 | CRUD          |
|                      |
| **Registered user**      | returning user           | R                                              | R                                           | R       | R                |  CRUD        | CRUD             | R (and copy) | CR              | N                 | CRUD          |
| **Site admin (backend)** | Django 'staff' users     | CRUD                                           | CRUD                                        | CRUD    | CRUD             | CRUD         | CRUD             | CRUD         | CRUD            | CRUD              | CRUD          |
|                      |
|                      |




### F03 RESPONSIVENESS	

### F04 NAVIGATION	
Screenprint - navbar - consistent

Meets requirements:
* FTU_01  As a **First-Time User** I want to **quickly understand the site purpose** so I **can decide whether to spend time exploring and discovering the site**
* FTU_02  As a **First-Time User** I want to **easily navigate the site** so I **don't become frustrated and leave**


### F05 CLEAR SITE PURPOSE/ EASE OF USE	
Screenprint - Landing page - clear call-to-action

### F06 USER FEEDBACK - TOASTS, EMAILS, SCREEN PROGRESSION	
Consistent use of logos, message styles and pop-ups
Screenprints:  Toast Messaging

Meets requirements:
* FTU_03 As a **First-Time User** I want to **receive feedback at each step on the site** so that I **understand what I am doing, and, if I'm in a multi-step process, I understand how far along I am in the processs**

### F03 Responsiveness:
Meets requirement:  * FTU_04 As a **First-Time User** I want to **access this site on a device of my choosing (mobile, tablet, laptop, desktop)** so that I can **access by a method and at a time that is convenient and accessible to me**

### F04 Ability to navigate the site without login

* FTU_05 As a **First-Time User** I want to **navigate the site without mandatory login** so **I can discover site features before deciding whether to commit to using site**
* SOXX Want to use the site as a shop window and welcome browsers who will complete the purchase pysically at the shop

### F07 - VIEW / SEARCH PRODUCTS	
### F08 - FILTER PRODUCTS	
### F09 - SORT PRODUCTS	
### F10 - PRODUCT DETAILS	
### F11 - PRODUCT REVIEWS	
### F12 - ABOUT PAGE/ USER FEEDBACK FORM	
### F13 - CREATE SHOPPING BASKET	
### F14 - CREATE ORDER FROM SHOPPING BASKET, including choosing delivery method	
### F15 - STRIPE PAYMENTS (WITH RESILIIENCE)	
### F16 - ORDER LIFECYCLE TRACKING, including ANPOST Tracking	
### F17 - PRODUCT LEAD TIMES	
### F18 - USER PROFILE CREATION & MAINTENANCE	
### F19 - EMAIL INTEGRATION	
### F20 - SYSADMIN PRODUCT MAINTENANCE	
### F21 - SYSADMIN - ORDER MAINTENANCE	
### F22 - NEWSLETTER & MARKETING, SOCIAL LINKS	
### F23 - SEARCH ENGINE OPTIMISTAION
### F24 - ERROR PAGES


Requirements Traceability Matrix - First-time Users



Requirements Traceability Matrix - Returning Users and System/Shop Owner


### Features in Scope 

<a href="https://github.com/DeeMcCart/Jeweller/blob/main/README_Features.md" target="_blank">Site features</a>

It was helpful to create this as a separate document, as it is also offered to users as a 'how to' guide.

### Implementation Decisions
Incremental delivery, 
Deployed early, 
Followed & adapted the Boutique walkthrough
Referenced additional Django walkthroughs and other materials
Used real-life verification from an Jewellery shop owner, who was clear on the features they prioritised

<br>  
Some of the site ideas and features needed only really became clear as I played with the site as it was delivered, and experienced frustration or spotted opportunites or elements that were worth adding. So the site grew organically as time went on.  The Agile approach with weekly sprints suits incremental development, as it encouraged weekly analysis of what had been done, and how it might progress.
<br>
There were quite a few 'false starts' when I tried to implement functionality and then found that it just didnt work in practice.  

Examples were:
* I envisaged building a rich cross-reference of product characteristics using category codes e.g. to store metal type (gold, silver, platinum etc); type of stone (diamond, tanzanite, garnet etc) and other characteristics which could be built into a search matrix, with dropdown searches per category for the customer.  However when I implemented this, I found it REALLY clunky to edit a product and to maintain the categories, and I also realised that the python q search functionality actually did a really good job of this type of searching (picks up any word or characters from product name/description).  So I backtracked and reversed out this detail.  I simplified the Product model as a result.  See .  [Link Text]([Link URL](https://github.com/DeeMcCart/CI_PP5_Jeweller/issues/31)) {target="_blank"}


* I intended do more with user addresses, and give the user the option to choose a shipping address, as I could see from the Stripe console that it had the concept of a billing & shipping address.  I modified the User Profile and Order data models to include an inline Address.  However when I looked at the order creation process, which is mirrored by a webhook, I could see that the order was being validated against a single-address model in Stripe's database.  This might be a future development with more time.  

* I implemented a model-based approach for the 'About' section, with sysadmin-editable inline text snippets (section -> title & seq# -> text body).  Originally I had thought that these might be edited using Summernote, which would allow for a rich 'About' and 'FAQ' section however summernote implementation is tricky for inline data structures so had to be moved outside the scope of the project.  The data models are in place and remain in use however they're just not as beautiful as i had hoped.

* Shipping lead time.  I wanted to implement some funtionality whereby  the user would be notified as to the likely despatch date for their order, and the concept of prioritising orders based on their shipping date, and to flagging up 'late' orders falling behind schedule.  I added a default lead time based on product source (stock = 1 day between order creation and shipping, make-to-order = 7 days, commisioned item = 21 days etc) with an editable value per product. Based in this i intended to calculate order/line shipping dates.  I added a method on the order model to determine if the order was 'late'.  This had to be backtracked as it was constantly re-evaluating 'late'ness of an order, and kept prompting as a changed order on every migration.
Shipping lead time is partially implemented witin the delivererd solution.








### Features Left to Implement
* FTU_28 (Future): As a **First-Time User** I would like to  **make an appointment for engagement rings** in order to **elevate a high value buying decision**
* 
               
## Technologies

### Langugages
- HTML 
- CSS
- Javascript
- Python
- Django (initial v 3, now V4+)
- Bootrap (V5)
- 

### Frameworks & Tools
* Github:  used to maintain the code repository, and for some readme edits and commits
* Git
* Gitpod:  used for editing and for tracking code commits back to Github
* Balsamiq:  used for wireframing
* Lucidchart: used for database diagramming & process flows
* Canva: used to create some infographic content
* Leonardo AI: used to create some of the site images


### Python Libraries/ Other external tools
The following additional python libraries were used:
* Bootstrap
* Allauth - code user authentication (extended)


### Third-Party Libraries



## Validation 

### Python Linting
There are 5 apps plus a project so approx 30 python files involved.  The approach taken to identifying and resolving python linting errors was to work through module-by-module using a command such as 'python3 -m flake8 APPNAME --exclude=APPNAME/migrations/'.  That way it was possible to systematically work through each of the app files and tick off each of the identified errors.
Of course, following the linting process means introducing more errors so it is a somewhat cyclical process.
Code not written directly by me (e.g. migrations within each app, Stripe snippets re-used) was not included in the linting validation, as not relevant for migrations which tend to have ultra-long lines and I was cautious about editing some of the template coding.

### HTML Validation 
- HTML
HTML validation was performed for the various site pages as follows:  Render the page via the app, right click on the page contents and take option to copy (rendered) source.  Paste this into a file and subject that file to the W3C validator.  

  - All errors returned from the validator were pursued and resolved.  Examples are shown below:
 
  on the index html pages when checked in the W3C validator:

![W3C Validator - index page](./jeweller/docs/readme_images/validation-w3c-index-html.png?raw=true "W3C validator (index page)")


![W3C validator - XX template ](./jeweller/docs/readme_images/validation-w3c-XXXX-html.png?raw=true "W3C validator (my planner page)")

![W3C validator - YY  template ](./jeweller/docs/readme_images/validation-w3c-XXXX-html.png?raw=true "W3C validator (my actions page)") 

![W3C validator - my_user page](./jeweller/docs/readme_images/validation-w3c-XXXX-html.png?raw=true "W3C validator (my actions page)") 

### CSS Validation

No errors returned when passing through the official Jigsaw validator.  

- ![(Jigaw) CSS Validator)](./jeweller/docs/readme_images/val-css.png?raw=true "CSS validator") 


### Performance
Performance for all pages was tested using the Lighthouse tool within Google Chrome.  Performance was at 98% for the index page (intro modal).


![Performance - Lighthouse - index](./jeweller/docs/readme_images/validation-lighthouse-performance-index-html1.png?raw=true "Lighthouse - index page") 


![Performance - article detail](./jeweller/docs/readme_images/validation-lighthouse-performance-article-detail-html.png?raw=true "Lighthouse - index page") 


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
![Feature testing page1](./jeweller/docs/readme_images/val-feature-p1.png?raw=true "Feature testing page1") 

![Feature testing page2](./jeweller/docs/readme_images/val-feature-p2.png?raw=true "Feature testing page2") 

![Feature testing page3](./jeweller/docs/readme_images/val-feature-p3.png?raw=true "Feature testing page3") 


### Bugs and issues
Almost XX issues were recorded, I used an excel spreadhseet to keep track.  

The structure of the log is shown here:

![Feature testing page3](./jeweller/docs/readme_images/val-issuelog.png?raw=true "Feature testing page3") 

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


### Content - Jeweller
* Existing Goldmark Jewellers website
* Existing Goldmark Jewellers marketing materials
* Review of other Jewellery websites
* Simone XXXX jeweller website was a particular inspiration

### Product images and descriptions
Goldmark facebook page

### References
* https://docs.allauth.org/en/latest/account/advanced.html extending the AllAuth User model
* https://docs.djangoproject.com/en/dev/topics/auth/customizing/ extending the AllAuth User model
* https://docs.allauth.org/en/latest/account/configuration.html to better understand AllAuth functionality
* Django 4 by Example: Build Powerful and Reliable web Applications from Scratch, Author:  XXXXXX
* https://stackoverflow.com/questions/77293705/i-am-building-a-product-review-app-in-my-django-ecommerce-project-i-cant-get-m
* https://www.youtube.com/watch?v=UgEVC7oJDHI Author:Desphisx, Creating Reviews and Star Rating Feature in Django
* https://www.geeksforgeeks.org/create-a-product-review-and-rating-system-using-html-css-and-javascript/ For product review entry & display
* Codemy.com used for YouTube learning re Extending the user model in Django python
* https://www.conventionalcommits.org/en/v1.0.0/#specification commit messages (recommendation from PP4 assessment team)



### Agile implementation in github
* https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-text-and-number-fields#adding-a-number-field to understand how story points might be represented in GitHub
 
### Code - Jeweller
DeeMac YouTube series - Setting up a Django receipe website
Book - 
Multiple Code Institute PP5 projects used for reference
 
### Acknowledgements
* I would particularly like to thank Alan Bushell, our cohort facilitator who has remained a steady consistent and wise presence during my 12 months on this programme.  His willingness to engage with each of us, his dedication to our weekly standups, his approachability and his guidance have been a huge support over this period.  
* I would like to sincerely thank my mentor, Mo Shami for his kindness, enthusiasm and support throughout.  Mo's ability to absorb the essence of a situation and to communicate a clear path ahead has been invaluable.
* Thank you also to the assessors who have given feedback on prevous projects
* I would also like to thank Derek and my family for their personal support, and for their advice on Goldmark business processes, help with system testing, and patience during my project-related absence!





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
