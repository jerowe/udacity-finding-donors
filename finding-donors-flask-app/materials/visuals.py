





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-lLo2nlsdl+bHLu6PGvC2j3wfP45RnK4wKQLiPnCDcuXfU38AiD+JCdMywnF3WbJC1jaxe3lAI6AM4uJuMFBLEw==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-08fc49d3bd2694c870ea23d0906f3610.css" />
  <link crossorigin="anonymous" media="all" integrity="sha512-+ZQwBfJw0+vWamxjWgu2B3g58zCABOB1yRj/kGGVcZmXuZ6wTWkVwNWaOgy285h5vdw4VuUp57FjdiVujwnkHw==" rel="stylesheet" href="https://github.githubassets.com/assets/github-b43e758c845fa54305d34a4b97d30922.css" />
  
  
  <link crossorigin="anonymous" media="all" integrity="sha512-ZxaEEWiQJEbxmw5l2qa5RiTSfE+MEeiyeENIUVl7q10lwwbZYkkTn2U4oi9nfHBR2l61Z2jGk6bNhlDWs0hOzQ==" rel="stylesheet" href="https://github.githubassets.com/assets/site-75fa15c3c296527ccae21da9e3bca74f.css" />
  
  

  <meta name="viewport" content="width=device-width">
  
  <title>machine-learning/visuals.py at master · udacity/machine-learning · GitHub</title>
    <meta name="description" content="Content for Udacity&#39;s Machine Learning curriculum. Contribute to udacity/machine-learning development by creating an account on GitHub.">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta property="og:image" content="https://avatars1.githubusercontent.com/u/1916665?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="udacity/machine-learning" /><meta property="og:url" content="https://github.com/udacity/machine-learning" /><meta property="og:description" content="Content for Udacity&#39;s Machine Learning curriculum. Contribute to udacity/machine-learning development by creating an account on GitHub." />

  <link rel="assets" href="https://github.githubassets.com/">
  
  <meta name="pjax-timeout" content="1000">
  
  <meta name="request-id" content="C264:3B27:29B7FD4:4F42DBA:5C29AFF7" data-pjax-transient>


  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

      <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="C264:3B27:29B7FD4:4F42DBA:5C29AFF7" /><meta name="octolytics-dimension-region_edge" content="iad" /><meta name="octolytics-dimension-region_render" content="iad" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-2">


<meta class="js-ga-set" name="dimension1" content="Logged Out">



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="YjY1YTczOGYxMGRlZWFkOTQ2NjAwNTEzYTZiODY5MzNiZDliZjM0M2VkYjdlOTQzMzU0MTUzOWUyZTc0NTUwZXx7InJlbW90ZV9hZGRyZXNzIjoiNzguMTAxLjE4NS4zMSIsInJlcXVlc3RfaWQiOiJDMjY0OjNCMjc6MjlCN0ZENDo0RjQyREJBOjVDMjlBRkY3IiwidGltZXN0YW1wIjoxNTQ2MjM1ODk1LCJob3N0IjoiZ2l0aHViLmNvbSJ9">

    <meta name="enabled-features" content="DASHBOARD_V2_LAYOUT_OPT_IN,EXPLORE_DISCOVER_REPOSITORIES,UNIVERSE_BANNER,MARKETPLACE_PLAN_RESTRICTION_EDITOR">

  <meta name="html-safe-nonce" content="354b28f5ec317d50446e13454a1b9eb2429fa2d9">

  <meta http-equiv="x-pjax-version" content="9a9575da25289c510f09170ac7c0c8d6">
  

      <link href="https://github.com/udacity/machine-learning/commits/master.atom" rel="alternate" title="Recent Commits to machine-learning:master" type="application/atom+xml">

  <meta name="go-import" content="github.com/udacity/machine-learning git https://github.com/udacity/machine-learning.git">

  <meta name="octolytics-dimension-user_id" content="1916665" /><meta name="octolytics-dimension-user_login" content="udacity" /><meta name="octolytics-dimension-repository_id" content="50450433" /><meta name="octolytics-dimension-repository_nwo" content="udacity/machine-learning" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="50450433" /><meta name="octolytics-dimension-repository_network_root_nwo" content="udacity/machine-learning" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


    <link rel="canonical" href="https://github.com/udacity/machine-learning/blob/master/projects/finding_donors/visuals.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://github.githubassets.com/favicon.ico">

<meta name="theme-color" content="#1e2327">



  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-out env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="px-2 py-4 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    


        
<header class="Header header-logged-out  position-relative f4 py-3" role="banner">
  <div class="container-lg d-flex px-3">
    <div class="d-flex flex-justify-between flex-items-center">
        <a class="mr-4" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark; experiment:site_header_dropdowns; group:dropdowns">
          <svg height="32" class="octicon octicon-mark-github text-white" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
        </a>
    </div>

    <div class="HeaderMenu HeaderMenu--logged-out d-flex flex-justify-between flex-items-center flex-auto">
      <div class="d-none">
        <button class="btn-link js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
          <svg height="24" class="octicon octicon-x text-gray" viewBox="0 0 12 16" version="1.1" width="18" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
        </button>
      </div>

        <nav class="mt-0" aria-label="Global">
          <ul class="d-flex list-style-none">
              <li class=" mr-3 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap  d-inline-block">
                    Why GitHub?
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-relative">
                      <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>
                  <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 mt-0  p-4 left-n4 position-absolute">
                    <a href="/features" class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Features">Features <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                    <ul class="list-style-none f5 pb-3">
                      <li class="edge-item-fix"><a href="/features/code-review/" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code review">Code review</a></li>
                      <li class="edge-item-fix"><a href="/features/project-management/" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Project management">Project management</a></li>
                      <li class="edge-item-fix"><a href="/features/integrations" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Integrations">Integrations</a></li>
                      <li class="edge-item-fix"><a href="/features#team-management" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Team management">Team management</a></li>
                      <li class="edge-item-fix"><a href="/features#social-coding" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Social coding">Social coding</a></li>
                      <li class="edge-item-fix"><a href="/features#documentation" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Documentation">Documentation</a></li>
                      <li class="edge-item-fix"><a href="/features#code-hosting" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code hosting">Code hosting</a></li>
                    </ul>

                    <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
                      <li class="edge-item-fix"><a href="/case-studies" class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Case studies">Case Studies <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                      <li class="edge-item-fix"><a href="/security" class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Security">Security <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                    </ul>
                  </div>
                </details>
              </li>
                <li class=" mr-3 mr-lg-3">
                  <a href="/business" class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Business">Business</a>
                </li>


              <li class=" mr-3 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap  d-inline-block">
                    Explore
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-relative">
                      <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>

                  <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-0 mt-0  p-4 left-n4 position-absolute">
                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="/explore" class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Features">Explore GitHub <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                    </ul>

                    <h4 class="text-gray-light text-normal text-mono f5 mb-2  border-top pt-3">Learn &amp; contribute</h4>
                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="/topics" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Topics">Topics</a></li>
                      <li class="edge-item-fix"><a href="/collections" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Collections">Collections</a></li>
                      <li class="edge-item-fix"><a href="/trending" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Trending">Trending</a></li>
                      <li class="edge-item-fix"><a href="https://lab.github.com/" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Learning lab">Learning Lab</a></li>
                      <li class="edge-item-fix"><a href="https://opensource.guide" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Open source guides">Open source guides</a></li>
                    </ul>

                    <h4 class="text-gray-light text-normal text-mono f5 mb-2  border-top pt-3">Connect with others</h4>
                    <ul class="list-style-none mb-0">
                      <li class="edge-item-fix"><a href="/events" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Events">Events</a></li>
                      <li class="edge-item-fix"><a href="https://github.community" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Community forum">Community forum</a></li>
                      <li class="edge-item-fix"><a href="https://education.github.com" class="py-2 pb-0 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to GitHub Education">GitHub Education</a></li>
                    </ul>
                  </div>
                </details>
              </li>

              <li class=" mr-3 mr-lg-3">
                <a href="/marketplace" class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Marketplace">Marketplace</a>
              </li>

              <li class=" mr-3 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap  d-inline-block">
                    Pricing
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-relative">
                       <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>

                  <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-4 mt-0  p-4 left-n4 position-absolute">
                    <a href="/pricing" class="pb-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Pricing">Plans <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>

                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="/pricing#feature-comparison" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Compare features">Compare plans</a></li>
                      <li class="edge-item-fix"><a href="https://enterprise.github.com/contact" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Compare features">Contact Sales</a></li>
                    </ul>

                    <ul class="list-style-none mb-0  border-top pt-3">
                      <li class="edge-item-fix"><a href="/nonprofit" class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Nonprofits">Nonprofit <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                      <li class="edge-item-fix"><a href="https://education.github.com/discount_requests/new" class="py-2 pb-0 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover"  data-ga-click="(Logged out) Header, go to Education">Education <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                    </ul>
                  </div>
                </details>
              </li>
          </ul>
        </nav>

      <div class="d-flex flex-items-center px-0 text-center text-left">
          <div class="d-lg-flex mr-3">
            <div class="header-search scoped-search site-scoped-search js-site-search position-relative js-jump-to"
  role="combobox"
  aria-owns="jump-to-results"
  aria-label="Search or jump to"
  aria-haspopup="listbox"
  aria-expanded="false"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" data-scope-type="Repository" data-scope-id="50450433" data-scoped-search-url="/udacity/machine-learning/search" data-unscoped-search-url="/search" action="/udacity/machine-learning/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control header-search-wrapper header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text"
          class="form-control header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search"
          data-unscoped-placeholder="Search GitHub"
          data-scoped-placeholder="Search"
          autocapitalize="off"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          aria-label="Search"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations#csrf-token=oAYH2hd2il1pYab9PxKQe5MsDRcceR+svyRVjMzke/0z+ODJsEOxsZUBX2t5ifhKVBT2zEPN6YY/DXi4SXYVXw=="
          spellcheck="false"
          autocomplete="off"
          >
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://github.githubassets.com/images/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="text-gray">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


</ul>

            </div>
      </label>
</form>  </div>
</div>

          </div>

        <a class="HeaderMenu-link no-underline mr-3" href="/login?return_to=%2Fudacity%2Fmachine-learning%2Fblob%2Fmaster%2Fprojects%2Ffinding_donors%2Fvisuals.py" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign&nbsp;in</a>
          <a class="HeaderMenu-link d-inline-block no-underline border border-gray-dark rounded-1 px-2 py-1" href="/join" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign&nbsp;up</a>
      </div>
    </div>
  </div>
</header>

  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">

</div>



  <div role="main" class="application-main " data-commit-hovercards-enabled>
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <div id="js-repo-pjax-container" data-pjax-container >
      


  


  



  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav  ">
    <div class="repohead-details-container clearfix container">

      <ul class="pagehead-actions">
  <li>
      <a href="/login?return_to=%2Fudacity%2Fmachine-learning"
    class="btn btn-sm btn-with-count tooltipped tooltipped-s"
    aria-label="You must be signed in to watch a repository" rel="nofollow">
    <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
    Watch
  </a>
  <a class="social-count" href="/udacity/machine-learning/watchers"
     aria-label="355 users are watching this repository">
    355
  </a>

  </li>

  <li>
        <a href="/login?return_to=%2Fudacity%2Fmachine-learning"
      class="btn btn-sm btn-with-count tooltipped tooltipped-s"
      aria-label="You must be signed in to star a repository" rel="nofollow">
      <svg class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
      Star
    </a>

    <a class="social-count js-social-count" href="/udacity/machine-learning/stargazers"
      aria-label="2511 users starred this repository">
      2,511
    </a>

  </li>

  <li>
      <a href="/login?return_to=%2Fudacity%2Fmachine-learning"
        class="btn btn-sm btn-with-count tooltipped tooltipped-s"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <svg class="octicon octicon-repo-forked v-align-text-bottom" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
        Fork
      </a>

    <a href="/udacity/machine-learning/network/members" class="social-count"
       aria-label="5130 users forked this repository">
      5,130
    </a>
  </li>
</ul>

      <h1 class="public ">
  <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a class="url fn" rel="author" data-hovercard-type="organization" data-hovercard-url="/orgs/udacity/hovercard" href="/udacity">udacity</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/udacity/machine-learning">machine-learning</a></strong>

</h1>

    </div>
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax container"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
    aria-label="Repository"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /udacity/machine-learning" href="/udacity/machine-learning">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /udacity/machine-learning/issues" href="/udacity/machine-learning/issues">
        <svg class="octicon octicon-issue-opened" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">11</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /udacity/machine-learning/pulls" href="/udacity/machine-learning/pulls">
      <svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">18</span>
      <meta itemprop="position" content="3">
</a>  </span>


    <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /udacity/machine-learning/projects" href="/udacity/machine-learning/projects">
      <svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>


    <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse alerts security /udacity/machine-learning/pulse" href="/udacity/machine-learning/pulse">
      <svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
      Insights
</a>

</nav>


  </div>

<div class="container new-discussion-timeline experiment-repo-nav  ">
  <div class="repository-content ">

    
    



  
    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/udacity/machine-learning/blob/7ba8bd66d491a31f1650f73f7a0d26ff619e20cd/projects/finding_donors/visuals.py">Permalink</a>

    <!-- blob contrib key: blob_contributors:v21:8a910db502f2665df1644e1bc1b79fb1 -->

        <div class="signup-prompt-bg rounded-1">
      <div class="signup-prompt p-4 text-center mb-4 rounded-1">
        <div class="position-relative">
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/site/dismiss_signup_prompt" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="S+mh61UxXtcQ/NDVdvINOxMXQ48VhSmXyS6G7dm87euqsIOPMXG2Gwl5cxPSEP4TZeTscuG+lZ5WqApniHhGJw==" />
            <button type="submit" class="position-absolute top-0 right-0 btn-link link-gray" data-ga-click="(Logged out) Sign up prompt, clicked Dismiss, text:dismiss">
              Dismiss
            </button>
</form>          <h3 class="pt-2">Join GitHub today</h3>
          <p class="col-6 mx-auto">GitHub is home to over 28 million developers working together to host and review code, manage projects, and build software together.</p>
          <a class="btn btn-primary" href="/join?source=prompt-blob-show" data-ga-click="(Logged out) Sign up prompt, clicked Sign up, text:sign-up">Sign up</a>
        </div>
      </div>
    </div>


    <div class="file-navigation">
      
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left "
  >
  <button class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" aria-expanded="false" aria-haspopup="true">
    <i>Branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>
    <div class="select-menu-modal">
        
<div class="select-menu-header">
  <svg class="octicon octicon-x js-menu-close" role="img" aria-label="Close" viewBox="0 0 12 16" version="1.1" width="12" height="16"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
  <span class="select-menu-title">Switch branches/tags</span>
</div>

<tab-container>
<div class="select-menu-filters">
  <div class="select-menu-text-filter">
    <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
  </div>
  <div class="select-menu-tabs" role="tablist">
    <ul>
      <li class="select-menu-tab">
        <button type="button" class="select-menu-tab-nav" data-filter-placeholder="Filter branches/tags" role="tab" aria-selected="true">Branches</button>
      </li>
      <li class="select-menu-tab">
        <button type="button" class="select-menu-tab-nav" data-filter-placeholder="Find a tag…" role="tab">Tags</button>
      </li>
    </ul>
  </div>
</div>

<div class="select-menu-list" role="tabpanel">
  <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">
      <a class="select-menu-item js-navigation-item js-navigation-open "
         href="/udacity/machine-learning/blob/development/projects/finding_donors/visuals.py"
         data-name="development"
         data-skip-pjax="true"
         rel="nofollow">
        <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
        <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
          development
        </span>
      </a>
      <a class="select-menu-item js-navigation-item js-navigation-open selected"
         href="/udacity/machine-learning/blob/master/projects/finding_donors/visuals.py"
         data-name="master"
         data-skip-pjax="true"
         rel="nofollow">
        <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
        <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
          master
        </span>
      </a>
      <a class="select-menu-item js-navigation-item js-navigation-open "
         href="/udacity/machine-learning/blob/nicky/remove-log-ignore/projects/finding_donors/visuals.py"
         data-name="nicky/remove-log-ignore"
         data-skip-pjax="true"
         rel="nofollow">
        <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
        <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
          nicky/remove-log-ignore
        </span>
      </a>
      <a class="select-menu-item js-navigation-item js-navigation-open "
         href="/udacity/machine-learning/blob/revert-170-master/projects/finding_donors/visuals.py"
         data-name="revert-170-master"
         data-skip-pjax="true"
         rel="nofollow">
        <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
        <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
          revert-170-master
        </span>
      </a>
      <a class="select-menu-item js-navigation-item js-navigation-open "
         href="/udacity/machine-learning/blob/smartcab-fix/projects/finding_donors/visuals.py"
         data-name="smartcab-fix"
         data-skip-pjax="true"
         rel="nofollow">
        <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
        <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
          smartcab-fix
        </span>
      </a>
      <a class="select-menu-item js-navigation-item js-navigation-open "
         href="/udacity/machine-learning/blob/test_normalize/projects/finding_donors/visuals.py"
         data-name="test_normalize"
         data-skip-pjax="true"
         rel="nofollow">
        <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
        <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
          test_normalize
        </span>
      </a>
  </div>

    <div class="select-menu-no-results">Nothing to show</div>
</div>

<div class="select-menu-list" role="tabpanel" hidden>
  <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">
  </div>

  <div class="select-menu-no-results">Nothing to show</div>
</div>
</tab-container>


    </div>
  </div>
</div>

      <div class="BtnGroup float-right">
        <a href="/udacity/machine-learning/find/master"
              class="js-pjax-capture-input btn btn-sm BtnGroup-item"
              data-pjax
              data-hotkey="t">
          Find file
        </a>
        <clipboard-copy for="blob-path" class="btn btn-sm BtnGroup-item">
          Copy path
        </clipboard-copy>
      </div>
      <div id="blob-path" class="breadcrumb">
        <span class="repo-root js-repo-root"><span class="js-path-segment"><a data-pjax="true" href="/udacity/machine-learning"><span>machine-learning</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/udacity/machine-learning/tree/master/projects"><span>projects</span></a></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/udacity/machine-learning/tree/master/projects/finding_donors"><span>finding_donors</span></a></span><span class="separator">/</span><strong class="final-path">visuals.py</strong>
      </div>
    </div>


    
  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/udacity/machine-learning/commit/117f68cee9e15d6c382cb8148e917f9733d452d7" data-pjax>
          117f68c
        </a>
        <relative-time datetime="2018-08-02T19:10:21Z">Aug 3, 2018</relative-time>
      </span>
      <div>
        <a rel="contributor" data-skip-pjax="true" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=41441668" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/DavidMachineLearning"><img class="avatar" src="https://avatars1.githubusercontent.com/u/41441668?s=40&amp;v=4" width="20" height="20" alt="@DavidMachineLearning" /></a>
        <a class="user-mention" rel="contributor" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=41441668" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/DavidMachineLearning">DavidMachineLearning</a>
          <a data-pjax="true" title="Fix on issue #340

Plots will come out with a good visualization now in Charity ML." class="message" href="/udacity/machine-learning/commit/117f68cee9e15d6c382cb8148e917f9733d452d7">Fix on issue</a> <a class="issue-link js-issue-link" data-error-text="Failed to load issue title" data-id="339671674" data-permission-text="Issue title is private" data-url="https://github.com/udacity/machine-learning/issues/340" data-hovercard-type="issue" data-hovercard-url="/udacity/machine-learning/issues/340/hovercard" href="https://github.com/udacity/machine-learning/issues/340">#340</a>
      </div>

    <div class="commit-tease-contributors">
      
<details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark float-left mr-2" id="blob_contributors_box">
  <summary class="btn-link" aria-haspopup="dialog"  >
    
    <span><strong>2</strong> contributors</span>
  </summary>
  <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast " aria-label="Users who have contributed to this file">
    <div class="Box-header">
      <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <h3 class="Box-title">Users who have contributed to this file</h3>
    </div>
    
        <ul class="list-style-none overflow-auto">
            <li class="Box-row">
              <a class="link-gray-dark no-underline" href="/DavidMachineLearning">
                <img class="avatar mr-2" alt="" src="https://avatars1.githubusercontent.com/u/41441668?s=40&amp;v=4" width="20" height="20" />
                DavidMachineLearning
</a>            </li>
            <li class="Box-row">
              <a class="link-gray-dark no-underline" href="/mattdeak">
                <img class="avatar mr-2" alt="" src="https://avatars3.githubusercontent.com/u/17998873?s=40&amp;v=4" width="20" height="20" />
                mattdeak
</a>            </li>
        </ul>

  </details-dialog>
</details>
          <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=41441668" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/udacity/machine-learning/commits/master/projects/finding_donors/visuals.py?author=DavidMachineLearning">
      <img class="avatar" src="https://avatars1.githubusercontent.com/u/41441668?s=40&amp;v=4" width="20" height="20" alt="@DavidMachineLearning" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=17998873" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/udacity/machine-learning/commits/master/projects/finding_donors/visuals.py?author=mattdeak">
      <img class="avatar" src="https://avatars3.githubusercontent.com/u/17998873?s=40&amp;v=4" width="20" height="20" alt="@mattdeak" /> 
</a>

    </div>
  </div>



    <div class="file ">
      
<div class="file-header">

  <div class="file-actions">


    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/udacity/machine-learning/raw/master/projects/finding_donors/visuals.py">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/udacity/machine-learning/blame/master/projects/finding_donors/visuals.py">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/udacity/machine-learning/commits/master/projects/finding_donors/visuals.py">History</a>
    </div>


        <button type="button" class="btn-octicon disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
        </button>
        <button type="button" class="btn-octicon btn-octicon-danger disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
        </button>
  </div>

  <div class="file-info">
      146 lines (119 sloc)
      <span class="file-info-divider"></span>
    5.17 KB
  </div>
</div>

      

  <div itemprop="text" class="blob-wrapper data type-python ">
      
<table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>##########################################</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Suppress matplotlib user warnings</span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Necessary for newer version of matplotlib</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> warnings</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line">warnings.filterwarnings(<span class="pl-s"><span class="pl-pds">&quot;</span>ignore<span class="pl-pds">&quot;</span></span>, <span class="pl-v">category</span> <span class="pl-k">=</span> <span class="pl-c1">UserWarning</span>, <span class="pl-v">module</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>matplotlib<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Display inline matplotlib plots with IPython</span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> IPython <span class="pl-k">import</span> get_ipython</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line">get_ipython().run_line_magic(<span class="pl-s"><span class="pl-pds">&#39;</span>matplotlib<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>inline<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>##########################################</span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> matplotlib.pyplot <span class="pl-k">as</span> pl</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> matplotlib.patches <span class="pl-k">as</span> mpatches</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> numpy <span class="pl-k">as</span> np</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> pandas <span class="pl-k">as</span> pd</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> time <span class="pl-k">import</span> time</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sklearn.metrics <span class="pl-k">import</span> f1_score, accuracy_score</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">distribution</span>(<span class="pl-smi">data</span>, <span class="pl-smi">transformed</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Visualization code for displaying skewed distributions of features</span></td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Create figure</span></td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">    fig <span class="pl-k">=</span> pl.figure(<span class="pl-v">figsize</span> <span class="pl-k">=</span> (<span class="pl-c1">11</span>,<span class="pl-c1">5</span>))<span class="pl-bu">;</span></td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Skewed feature plotting</span></td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> i, feature <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>([<span class="pl-s"><span class="pl-pds">&#39;</span>capital-gain<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>capital-loss<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">        ax <span class="pl-k">=</span> fig.add_subplot(<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, i<span class="pl-k">+</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">        ax.hist(data[feature], <span class="pl-v">bins</span> <span class="pl-k">=</span> <span class="pl-c1">25</span>, <span class="pl-v">color</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>#00A0A0<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">        ax.set_title(<span class="pl-s"><span class="pl-pds">&quot;</span>&#39;<span class="pl-c1">%s</span>&#39; Feature Distribution<span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(feature), <span class="pl-v">fontsize</span> <span class="pl-k">=</span> <span class="pl-c1">14</span>)</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">        ax.set_xlabel(<span class="pl-s"><span class="pl-pds">&quot;</span>Value<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">        ax.set_ylabel(<span class="pl-s"><span class="pl-pds">&quot;</span>Number of Records<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">        ax.set_ylim((<span class="pl-c1">0</span>, <span class="pl-c1">2000</span>))</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">        ax.set_yticks([<span class="pl-c1">0</span>, <span class="pl-c1">500</span>, <span class="pl-c1">1000</span>, <span class="pl-c1">1500</span>, <span class="pl-c1">2000</span>])</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">        ax.set_yticklabels([<span class="pl-c1">0</span>, <span class="pl-c1">500</span>, <span class="pl-c1">1000</span>, <span class="pl-c1">1500</span>, <span class="pl-s"><span class="pl-pds">&quot;</span>&gt;2000<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Plot aesthetics</span></td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> transformed:</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">        fig.suptitle(<span class="pl-s"><span class="pl-pds">&quot;</span>Log-transformed Distributions of Continuous Census Data Features<span class="pl-pds">&quot;</span></span>, \</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">fontsize</span> <span class="pl-k">=</span> <span class="pl-c1">16</span>, <span class="pl-v">y</span> <span class="pl-k">=</span> <span class="pl-c1">1.03</span>)</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">        fig.suptitle(<span class="pl-s"><span class="pl-pds">&quot;</span>Skewed Distributions of Continuous Census Data Features<span class="pl-pds">&quot;</span></span>, \</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">fontsize</span> <span class="pl-k">=</span> <span class="pl-c1">16</span>, <span class="pl-v">y</span> <span class="pl-k">=</span> <span class="pl-c1">1.03</span>)</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">    fig.tight_layout()</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">    fig.show()</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">evaluate</span>(<span class="pl-smi">results</span>, <span class="pl-smi">accuracy</span>, <span class="pl-smi">f1</span>):</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Visualization code to display results of various learners.</span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    </span></td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    inputs:</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      - learners: a list of supervised learners</span></td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      - stats: a list of dictionaries of the statistic results from &#39;train_predict()&#39;</span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      - accuracy: The score for the naive predictor</span></td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      - f1: The score for the naive predictor</span></td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">  </td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Create figure</span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">    fig, ax <span class="pl-k">=</span> pl.subplots(<span class="pl-c1">2</span>, <span class="pl-c1">4</span>, <span class="pl-v">figsize</span> <span class="pl-k">=</span> (<span class="pl-c1">11</span>,<span class="pl-c1">7</span>))</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Constants</span></td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">    bar_width <span class="pl-k">=</span> <span class="pl-c1">0.3</span></td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">    colors <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>#A00000<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>#00A0A0<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>#00A000<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Super loop to plot four panels of data</span></td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> k, learner <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(results.keys()):</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> j, metric <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>([<span class="pl-s"><span class="pl-pds">&#39;</span>train_time<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>acc_train<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>f_train<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>pred_time<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>acc_test<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>f_test<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> i <span class="pl-k">in</span> np.arange(<span class="pl-c1">3</span>):</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">                </td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> Creative plot code</span></td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">                ax[j<span class="pl-k">//</span><span class="pl-c1">3</span>, j<span class="pl-k">%</span><span class="pl-c1">3</span>].bar(i<span class="pl-k">+</span>k<span class="pl-k">*</span>bar_width, results[learner][i][metric], <span class="pl-v">width</span> <span class="pl-k">=</span> bar_width, <span class="pl-v">color</span> <span class="pl-k">=</span> colors[k])</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">                ax[j<span class="pl-k">//</span><span class="pl-c1">3</span>, j<span class="pl-k">%</span><span class="pl-c1">3</span>].set_xticks([<span class="pl-c1">0.45</span>, <span class="pl-c1">1.45</span>, <span class="pl-c1">2.45</span>])</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">                ax[j<span class="pl-k">//</span><span class="pl-c1">3</span>, j<span class="pl-k">%</span><span class="pl-c1">3</span>].set_xticklabels([<span class="pl-s"><span class="pl-pds">&quot;</span>1%<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>10%<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>100%<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">                ax[j<span class="pl-k">//</span><span class="pl-c1">3</span>, j<span class="pl-k">%</span><span class="pl-c1">3</span>].set_xlabel(<span class="pl-s"><span class="pl-pds">&quot;</span>Training Set Size<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">                ax[j<span class="pl-k">//</span><span class="pl-c1">3</span>, j<span class="pl-k">%</span><span class="pl-c1">3</span>].set_xlim((<span class="pl-k">-</span><span class="pl-c1">0.1</span>, <span class="pl-c1">3.0</span>))</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Add unique y-labels</span></td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">0</span>, <span class="pl-c1">0</span>].set_ylabel(<span class="pl-s"><span class="pl-pds">&quot;</span>Time (in seconds)<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">0</span>, <span class="pl-c1">1</span>].set_ylabel(<span class="pl-s"><span class="pl-pds">&quot;</span>Accuracy Score<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">0</span>, <span class="pl-c1">2</span>].set_ylabel(<span class="pl-s"><span class="pl-pds">&quot;</span>F-score<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">1</span>, <span class="pl-c1">0</span>].set_ylabel(<span class="pl-s"><span class="pl-pds">&quot;</span>Time (in seconds)<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">1</span>, <span class="pl-c1">1</span>].set_ylabel(<span class="pl-s"><span class="pl-pds">&quot;</span>Accuracy Score<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">1</span>, <span class="pl-c1">2</span>].set_ylabel(<span class="pl-s"><span class="pl-pds">&quot;</span>F-score<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Add titles</span></td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">0</span>, <span class="pl-c1">0</span>].set_title(<span class="pl-s"><span class="pl-pds">&quot;</span>Model Training<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">0</span>, <span class="pl-c1">1</span>].set_title(<span class="pl-s"><span class="pl-pds">&quot;</span>Accuracy Score on Training Subset<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">0</span>, <span class="pl-c1">2</span>].set_title(<span class="pl-s"><span class="pl-pds">&quot;</span>F-score on Training Subset<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">1</span>, <span class="pl-c1">0</span>].set_title(<span class="pl-s"><span class="pl-pds">&quot;</span>Model Predicting<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">1</span>, <span class="pl-c1">1</span>].set_title(<span class="pl-s"><span class="pl-pds">&quot;</span>Accuracy Score on Testing Set<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">1</span>, <span class="pl-c1">2</span>].set_title(<span class="pl-s"><span class="pl-pds">&quot;</span>F-score on Testing Set<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Add horizontal lines for naive predictors</span></td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">0</span>, <span class="pl-c1">1</span>].axhline(<span class="pl-v">y</span> <span class="pl-k">=</span> accuracy, <span class="pl-v">xmin</span> <span class="pl-k">=</span> <span class="pl-k">-</span><span class="pl-c1">0.1</span>, <span class="pl-v">xmax</span> <span class="pl-k">=</span> <span class="pl-c1">3.0</span>, <span class="pl-v">linewidth</span> <span class="pl-k">=</span> <span class="pl-c1">1</span>, <span class="pl-v">color</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>k<span class="pl-pds">&#39;</span></span>, <span class="pl-v">linestyle</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>dashed<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">1</span>, <span class="pl-c1">1</span>].axhline(<span class="pl-v">y</span> <span class="pl-k">=</span> accuracy, <span class="pl-v">xmin</span> <span class="pl-k">=</span> <span class="pl-k">-</span><span class="pl-c1">0.1</span>, <span class="pl-v">xmax</span> <span class="pl-k">=</span> <span class="pl-c1">3.0</span>, <span class="pl-v">linewidth</span> <span class="pl-k">=</span> <span class="pl-c1">1</span>, <span class="pl-v">color</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>k<span class="pl-pds">&#39;</span></span>, <span class="pl-v">linestyle</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>dashed<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">0</span>, <span class="pl-c1">2</span>].axhline(<span class="pl-v">y</span> <span class="pl-k">=</span> f1, <span class="pl-v">xmin</span> <span class="pl-k">=</span> <span class="pl-k">-</span><span class="pl-c1">0.1</span>, <span class="pl-v">xmax</span> <span class="pl-k">=</span> <span class="pl-c1">3.0</span>, <span class="pl-v">linewidth</span> <span class="pl-k">=</span> <span class="pl-c1">1</span>, <span class="pl-v">color</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>k<span class="pl-pds">&#39;</span></span>, <span class="pl-v">linestyle</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>dashed<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">1</span>, <span class="pl-c1">2</span>].axhline(<span class="pl-v">y</span> <span class="pl-k">=</span> f1, <span class="pl-v">xmin</span> <span class="pl-k">=</span> <span class="pl-k">-</span><span class="pl-c1">0.1</span>, <span class="pl-v">xmax</span> <span class="pl-k">=</span> <span class="pl-c1">3.0</span>, <span class="pl-v">linewidth</span> <span class="pl-k">=</span> <span class="pl-c1">1</span>, <span class="pl-v">color</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>k<span class="pl-pds">&#39;</span></span>, <span class="pl-v">linestyle</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>dashed<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Set y-limits for score panels</span></td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">0</span>, <span class="pl-c1">1</span>].set_ylim((<span class="pl-c1">0</span>, <span class="pl-c1">1</span>))</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">0</span>, <span class="pl-c1">2</span>].set_ylim((<span class="pl-c1">0</span>, <span class="pl-c1">1</span>))</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">1</span>, <span class="pl-c1">1</span>].set_ylim((<span class="pl-c1">0</span>, <span class="pl-c1">1</span>))</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">1</span>, <span class="pl-c1">2</span>].set_ylim((<span class="pl-c1">0</span>, <span class="pl-c1">1</span>))</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Set additional plots invisibles</span></td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">0</span>, <span class="pl-c1">3</span>].set_visible(<span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">    ax[<span class="pl-c1">1</span>, <span class="pl-c1">3</span>].axis(<span class="pl-s"><span class="pl-pds">&#39;</span>off<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Create legend</span></td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> i, learner <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(results.keys()):</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">        pl.bar(<span class="pl-c1">0</span>, <span class="pl-c1">0</span>, <span class="pl-v">color</span><span class="pl-k">=</span>colors[i], <span class="pl-v">label</span><span class="pl-k">=</span>learner)</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">    pl.legend()</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Aesthetics</span></td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">    pl.suptitle(<span class="pl-s"><span class="pl-pds">&quot;</span>Performance Metrics for Three Supervised Learning Models<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fontsize</span> <span class="pl-k">=</span> <span class="pl-c1">16</span>, <span class="pl-v">y</span> <span class="pl-k">=</span> <span class="pl-c1">1.10</span>)</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">    pl.tight_layout()</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">    pl.show()</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">feature_plot</span>(<span class="pl-smi">importances</span>, <span class="pl-smi">X_train</span>, <span class="pl-smi">y_train</span>):</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Display the five most important features</span></td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">    indices <span class="pl-k">=</span> np.argsort(importances)[::<span class="pl-k">-</span><span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">    columns <span class="pl-k">=</span> X_train.columns.values[indices[:<span class="pl-c1">5</span>]]</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">    values <span class="pl-k">=</span> importances[indices][:<span class="pl-c1">5</span>]</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Creat the plot</span></td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">    fig <span class="pl-k">=</span> pl.figure(<span class="pl-v">figsize</span> <span class="pl-k">=</span> (<span class="pl-c1">9</span>,<span class="pl-c1">5</span>))</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">    pl.title(<span class="pl-s"><span class="pl-pds">&quot;</span>Normalized Weights for First Five Most Predictive Features<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fontsize</span> <span class="pl-k">=</span> <span class="pl-c1">16</span>)</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">    pl.bar(np.arange(<span class="pl-c1">5</span>), values, <span class="pl-v">width</span> <span class="pl-k">=</span> <span class="pl-c1">0.6</span>, <span class="pl-v">align</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>center<span class="pl-pds">&quot;</span></span>, <span class="pl-v">color</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>#00A000<span class="pl-pds">&#39;</span></span>, \</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">          <span class="pl-v">label</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Feature Weight<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">    pl.bar(np.arange(<span class="pl-c1">5</span>) <span class="pl-k">-</span> <span class="pl-c1">0.3</span>, np.cumsum(values), <span class="pl-v">width</span> <span class="pl-k">=</span> <span class="pl-c1">0.2</span>, <span class="pl-v">align</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>center<span class="pl-pds">&quot;</span></span>, <span class="pl-v">color</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>#00A0A0<span class="pl-pds">&#39;</span></span>, \</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">          <span class="pl-v">label</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Cumulative Feature Weight<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">    pl.xticks(np.arange(<span class="pl-c1">5</span>), columns)</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">    pl.xlim((<span class="pl-k">-</span><span class="pl-c1">0.5</span>, <span class="pl-c1">4.5</span>))</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">    pl.ylabel(<span class="pl-s"><span class="pl-pds">&quot;</span>Weight<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fontsize</span> <span class="pl-k">=</span> <span class="pl-c1">12</span>)</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">    pl.xlabel(<span class="pl-s"><span class="pl-pds">&quot;</span>Feature<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fontsize</span> <span class="pl-k">=</span> <span class="pl-c1">12</span>)</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">    pl.legend(<span class="pl-v">loc</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>upper center<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">    pl.tight_layout()</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">    pl.show()  </td>
      </tr>
</table>

  <details class="details-reset details-overlay BlobToolbar position-absolute js-file-line-actions dropdown d-none" aria-hidden="true">
    <summary class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1" aria-label="Inline file action toolbar">
      <svg class="octicon octicon-kebab-horizontal" viewBox="0 0 13 16" version="1.1" width="13" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zm5 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zM13 7.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/></svg>
    </summary>
    <details-menu>
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2">
        <li><clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-lines" style="cursor:pointer;" data-original-text="Copy lines">Copy lines</clipboard-copy></li>
        <li><clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;" data-original-text="Copy permalink">Copy permalink</clipboard-copy></li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" role="menuitem" href="/udacity/machine-learning/blame/7ba8bd66d491a31f1650f73f7a0d26ff619e20cd/projects/finding_donors/visuals.py">View git blame</a></li>
          <li><a class="dropdown-item" id="js-new-issue" role="menuitem" href="/udacity/machine-learning/issues/new">Open new issue</a></li>
      </ul>
    </details-menu>
  </details>

  </div>

    </div>

  

  <details class="details-reset details-overlay details-overlay-dark">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>



  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

        
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2018 <span title="0.16468s from unicorn-6884bf5549-cstf2">GitHub</span>, Inc.</li>
        <li class="mr-3"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3"><a href="/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li class="mr-3"><a href="https://githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-lg-4" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3"><a href="https://blog.github.com" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    <script crossorigin="anonymous" integrity="sha512-WnyO4VoIUwWWQOmFLjYf4UGg/c1z9VlaLN8IMuiI3uMhhl6rejyThRdLPDyePeUPW6N+38OoBMs6AkqcvWALtA==" type="application/javascript" src="https://github.githubassets.com/assets/compat-b66b5d97b4442a01f057c74b091c4368.js"></script>
    <script crossorigin="anonymous" integrity="sha512-qj1Z4g+YDVWKElb6FC42CcUWNq8P0W9aiU0CtKWjzuEMO9tb8sbbJ48dWUkmaOIe7WlLJXkI4YsUCKMxRMxT5A==" type="application/javascript" src="https://github.githubassets.com/assets/frameworks-9ee26246cce2c45ef24accded28cdabe.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-YK1qKaJaboZghfxUvkZpVcxPUUE74mJclzBlt7BcsMQp37KQFQCIjO9ySZpwS3FdiPv2pmTEs5qakCIlGRVGwA==" type="application/javascript" src="https://github.githubassets.com/assets/github-f64ad9727bd629401c830ad67cd20b4c.js"></script>
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
  </div>
</div>

  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark" open>
    <summary aria-haspopup="dialog" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

<div id="hovercard-aria-description" class="sr-only">
  Press h to open a hovercard with more details.
</div>

  <div aria-live="polite" class="js-global-screen-reader-notice sr-only"></div>

  </body>
</html>

