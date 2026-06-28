# Sanity

> Sanity is a Content Operating System for the AI era. It provides the structured foundation, automation layer, and agentic context companies need to move faster, work smarter, and power every content experience—from websites to AI agents.

## Docs

### Blueprints

- [Manage Sanity with code](https://www.sanity.io/docs/blueprints): Blueprints let you have infrastructure-as-code level management for your Sanity resources.
- [Blueprints introduction](https://www.sanity.io/docs/blueprints/blueprints-introduction): Learn what Blueprints are, how they work, and how to get started.
- [Project layout and monorepos](https://www.sanity.io/docs/blueprints/project-layout-and-monorepos): Lay out a Sanity project so Blueprints, Functions, and your application code coexist cleanly in monorepos.
- [Deploy Blueprints with GitHub Actions](https://www.sanity.io/docs/blueprints/blueprint-action): Use the official action to deploy your blueprints with GitHub Actions.
- [Define a webhook with Blueprints](https://www.sanity.io/docs/blueprints/blueprints-webhook): Blueprints allow you to define and manage your webhooks in code, then deploy them in a predictable manner.
- [Define a CORS origin with Blueprints](https://www.sanity.io/docs/blueprints/blueprints-cors): Blueprints allow you to define and manage your CORS origins in code, then deploy them in a predictable manner.
- [Define a robot token with Blueprints](https://www.sanity.io/docs/blueprints/blueprints-robot-tokens): Blueprints allow you to create robot tokens alongside other resources for use in the blueprint.
- [Define a role with Blueprints](https://www.sanity.io/docs/blueprints/blueprints-role): Use Blueprints to define a custom role in code alongside your project's other resources.
- [Promote a stack to organization scope](https://www.sanity.io/docs/blueprints/promote-stack-to-organization-scope): Learn how to promote an existing project-scoped blueprint stack to organization scope to unlock scheduled functions.
- [Blueprint configuration reference](https://www.sanity.io/docs/blueprints/blueprint-config): Reference documentation for the Blueprint configuration files.
- [Blueprints CLI command reference](https://www.sanity.io/docs/cli-reference/cli-blueprints): Reference documentation for the Sanity CLI Blueprints command.

### Functions

- [Deploy custom functions to automate content operations](https://www.sanity.io/docs/functions): Sanity Functions enable you to execute custom logic whenever changes occur in your content—all without requiring your own infrastructure.
- [Functions](https://www.sanity.io/docs/functions/functions-introduction): Learn how to take advantage of Functions in your Sanity projects.
- [Create a Document Function](https://www.sanity.io/docs/functions/function-quickstart): Start building with Functions by deploying a new function to Sanity's infrastructure.
- [Create a Media Library Asset Function](https://www.sanity.io/docs/functions/asset-function-quickstart): Start building a function that reacts to changes to a Media Library asset.
- [Create a Sync Tag Invalidate Function](https://www.sanity.io/docs/functions/sync-tag-function-quickstart): Build and deploy a new Sync Tag Invalidate function to Sanity's infrastructure.
- [Create a Scheduled Function](https://www.sanity.io/docs/functions/scheduled-function-quickstart): Create your first scheduled function, a Sanity function that runs on a set schedule, with Blueprints.
- [Manage function dependencies](https://www.sanity.io/docs/functions/function-dependencies): Functions can be self-contained, or part of a larger ecosystem. Learn how to manage function dependencies in your projects.
- [Testing functions locally](https://www.sanity.io/docs/functions/functions-local-testing): Simulate Functions locally with real data and an interactive playground.
- [Configure @sanity/client in Functions](https://www.sanity.io/docs/functions/functions-js-client): Learn to use the JavaScript client in a Sanity Function.
- [Add environment variables to functions](https://www.sanity.io/docs/functions/function-env-vars): Learn to add environment variables to Functions.
- [Using robot tokens with Functions](https://www.sanity.io/docs/functions/robot-tokens-with-functions): Learn how to authenticate Sanity Functions using robot tokens defined with Blueprints.
- [Functions cheat sheet](https://www.sanity.io/docs/functions/functions-cheatsheet): Common patterns and techniques for creating Functions.
- [Function handler reference](https://www.sanity.io/docs/functions/function-wrapper): Reference documentation for the shape of the function wrapper.
- [Functions CLI command reference](https://www.sanity.io/docs/cli-reference/functions): Interact with and test your Sanity Functions from the CLI.

### Canvas

- [Canvas](https://www.sanity.io/docs/canvas): A place to author content that embraces the creative process and helps you deliver better and faster with seamless hand-off to your front end. Work with templates, an AI ghostwriter, and map content back to Studio.
- [Introduction to Canvas](https://www.sanity.io/docs/canvas/introduction-to-canvas): A familiar writing tool that understands your content structure, so content can flow directly into the right Studio fields with a single click.
- [Writing in Canvas](https://www.sanity.io/docs/canvas/writing): Write and collaborate in Canvas with AI assistance, contextual notes, and real-time collaboration.
- [Keyboard shortcuts](https://www.sanity.io/docs/canvas/keyboard-shortcuts): Reference for Canvas keyboard shortcuts covering text formatting, document navigation, text selection, document management, collaboration, and Canvas-specific features.
- [Working with templates](https://www.sanity.io/docs/canvas/templates): Create reusable Canvas templates with pre-configured content types and field labels for repeatable content workflows.
- [Troubleshooting Canvas](https://www.sanity.io/docs/canvas/troubleshooting): Common issues writers run into when using Canvas, with suggested fixes.
- [Configure Canvas for your content](https://www.sanity.io/docs/canvas/configure-canvas): Make your Studio schema available in Canvas and configure how it surfaces to writers.

### Build with AI

- [Build with AI](https://www.sanity.io/docs/ai): AI-powered tools to enhance your content and development workflows.
- [Get started with AI-powered Sanity development](https://www.sanity.io/docs/ai/ai-quickstart): Set up the Sanity Agent Toolkit and MCP server to help AI assistants generate high-quality Sanity code that follows established best practices.
- [Sanity MCP server](https://www.sanity.io/docs/ai/mcp-server): Connect AI to Sanity via MCP. Learn to install the server, link your IDE, and safely query or update content through developer and editor endpoints.
- [Agent Skills](https://www.sanity.io/docs/ai/skills): Understand and use agent skills to help AI assistants generate high-quality Sanity code that follows established best practices.
- [Sanity Context](https://www.sanity.io/docs/ai/sanity-context): Sanity Context is a hosted Model Context Protocol (MCP) server that gives AI agents structured, read-only access to a Sanity dataset.
- [Add insights to Sanity Context](https://www.sanity.io/docs/ai/sanity-context-insights): Sanity Context insights tracks and analyzes your agent conversations
- [Content Agent API](https://www.sanity.io/docs/apis-and-sdks/content-agent-api): Build custom integrations with the Sanity Content Agent API.
- [Install and configure Sanity AI Assist](https://www.sanity.io/docs/studio/install-and-configure-sanity-ai-assist): How to install and configure the AI Assist plugin for Sanity Studio.

### HTTP API Reference

- [HTTP API Reference](https://www.sanity.io/docs/reference): The HTTP API endpoints offer direct access to the same APIs used by the Sanity Client, Studio, and other apps to interact with Content Lake and the greater Sanity ecosystem.
- [Actions API reference](https://www.sanity.io/docs/http-reference/actions): Reference documentation for the Actions HTTP endpoint.
- [Assets API reference](https://www.sanity.io/docs/http-reference/assets): Upload images and files to Content Lake, and link Media Library assets to your dataset.
- [Copy API reference](https://www.sanity.io/docs/http-reference/copy): The Copy API, or Cloud Clone, lets you copy existing datasets.
- [Backups API reference](https://www.sanity.io/docs/http-reference/backups): Reference documentation for the Backups API.
- [Doc API reference](https://www.sanity.io/docs/http-reference/doc): Retrieve one or more documents by ID and bypass the caching layer.
- [Export API reference](https://www.sanity.io/docs/http-reference/export): Reference documentation for the export HTTP endpoint.
- [History API reference](https://www.sanity.io/docs/http-reference/history): Reference documentation for the History HTTP endpoint.
- [Jobs API reference](https://www.sanity.io/docs/http-reference/jobs): Reference documentation for the Jobs HTTP endpoint.
- [Listen API reference](https://www.sanity.io/docs/http-reference/listen): Reference documentation for the Listen HTTP endpoint.
- [Live Content API reference](https://www.sanity.io/docs/http-reference/live): Reference documentation for the Live HTTP endpoint.
- [Mutation API reference](https://www.sanity.io/docs/http-reference/mutation): Reference documentation for the Mutatation HTTP reference.
- [Query API reference](https://www.sanity.io/docs/http-reference/query): Reference documentation for the Query HTTP endpoint.
- [Scheduling API reference](https://www.sanity.io/docs/http-reference/scheduling): Reference documentation for the Scheduling HTTP endpoints.
- [Webhooks API reference](https://www.sanity.io/docs/http-reference/webhooks): Reference documentation for the Webhooks HTTP endpoints.
- [Agent Actions](https://www.sanity.io/docs/http-reference/agent-actions): Reference documentation for the Agent Actions HTTP API.
- [Embeddings Index API reference](https://www.sanity.io/docs/http-reference/embeddings-index): Reference documentation for the Embeddings Index HTTP endpoints.
- [Content Agent API reference](https://www.sanity.io/docs/http-reference/content-agent): HTTP reference documentation for the Content Agent API
- [Media Library API reference](https://www.sanity.io/docs/http-reference/media-library): HTTP endpoints reference for the Media Library API
- [Access API reference](https://www.sanity.io/docs/http-reference/access-api): A centralized API to manage resource access control through roles and permissions.
- [Projects API reference](https://www.sanity.io/docs/http-reference/projects-api): Reference documentation for the projects HTTP endpoint.
- [Roles API reference](https://www.sanity.io/docs/http-reference/roles): Reference documentation for the Roles HTTP endpoints.
- [User attributes API reference](https://www.sanity.io/docs/http-reference/user-attributes): Manage user attributes and attribute definitions to enable parameterized role-based access control

### Libraries

- [Libraries and tooling](https://www.sanity.io/docs/libraries): Integrate your content with applications and front end frameworks. Use specialized tooling for customization and working with content as data.
- [Embeddings Index CLI reference](https://www.sanity.io/docs/libraries/embeddings-index-cli-reference): Reference documentation of the Sanity Embeddings Index CLI to create and manage embeddings indexes for your content.

### Specifications

- [Specifications](https://www.sanity.io/docs/specifications): Specifications and standards used throughout the Sanity ecosystem and maintained by the Sanity team.
- [GROQ syntax](https://www.sanity.io/docs/specifications/groq-syntax): Reference documentation for the GROQ syntax.
- [GROQ data types](https://www.sanity.io/docs/specifications/groq-data-types): Data types supported by GROQ
- [GROQ parameters](https://www.sanity.io/docs/specifications/groq-parameters): User-provided parameters in GROQ
- [GROQ operators](https://www.sanity.io/docs/specifications/groq-operators): A description of operators in GROQ
- [GROQ functions reference](https://www.sanity.io/docs/specifications/groq-functions): Reference documentation for GROQ functions.
- [GROQ pipeline components](https://www.sanity.io/docs/specifications/groq-pipeline-components): A description of GROQ pipeline components
- [GROQ joins](https://www.sanity.io/docs/specifications/groq-joins): A description of joining multiple documents in GROQ
- [Function handler reference](https://www.sanity.io/docs/functions/function-wrapper): Reference documentation for the shape of the function wrapper.
- [Blueprint configuration reference](https://www.sanity.io/docs/blueprints/blueprint-config): Reference documentation for the Blueprint configuration files.

### Visual Editing

- [Visual Editing](https://www.sanity.io/docs/visual-editing): Visual Editing lets content creators see their changes live and edit content directly from the webpage. Think of it as a bridge between your Sanity Studio and your website. Your content team can view drafts, click and drag elements to edit them, and see changes in real-time.
- [Visual editing](https://www.sanity.io/docs/visual-editing/introduction-to-visual-editing): Framework quickstarts, a framework-agnostic conceptual series, and task-focused guides for specific features.
- [Visual Editing with Next.js App Router](https://www.sanity.io/docs/visual-editing/visual-editing-with-next-js-app-router): Set up visual editing between Sanity Studio and a Next.js App Router frontend, including the Sanity client, Draft Mode, Visual Editing, and Live Content.
- [Visual Editing with Next.js Pages Router](https://www.sanity.io/docs/visual-editing/visual-editing-with-next-js-pages-router): Get started with Sanity Visual Editing in a new or existing Next.js application using the Pages Router.
- [Visual Editing with Nuxt](https://www.sanity.io/docs/visual-editing/visual-editing-with-nuxt): Get started with Sanity Visual Editing in a new or existing Nuxt application.
- [Visual Editing with SvelteKit](https://www.sanity.io/docs/visual-editing/visual-editing-with-sveltekit): Get started with Sanity Visual Editing in a new or existing SvelteKit application.
- [Visual Editing with React Router/Remix ](https://www.sanity.io/docs/visual-editing/visual-editing-with-react-router): Get started with Sanity Visual Editing in a new or existing React Router (Remix) application.
- [Visual Editing with React Native](https://www.sanity.io/docs/visual-editing/visual-editing-with-react-native): Get started with Sanity Visual Editing in a new or existing React Native application using the Sanity React Loader.
- [Visual Editing with Astro](https://www.sanity.io/docs/visual-editing/astro-visual-editing): Configure Sanity’s Presentation Tool, draft mode, and visual editing overlays to work with an Astro 6 server-rendered frontend.
- [Visual editing architecture overview](https://www.sanity.io/docs/visual-editing/visual-editing-architecture): Understand how Sanity's visual editing works across six architectural layers: content source maps, stega encoding, overlays, live updates, preview mode, and the Presentation Tool.
- [Configuring the Presentation Tool](https://www.sanity.io/docs/visual-editing/configuring-the-presentation-tool): Configure the Presentation Tool: previewUrl, document location resolvers, allowed origins, components, and navigation for multi-environment setups.
- [Client setup and stega for visual editing](https://www.sanity.io/docs/visual-editing/visual-editing-client-stega): Configure the Sanity client for visual editing: stega encoding, Content Source Maps, perspectives, and secure token handling.
- [Implementing draft mode](https://www.sanity.io/docs/visual-editing/implementing-draft-mode): Implement secure draft mode from scratch using @sanity/preview-url-secret and standard Web APIs, with draft mode cookies, validation, and framework-agnostic endpoints.
- [Live preview content updates](https://www.sanity.io/docs/visual-editing/live-preview-content-updates): Build real-time content updates using the core-loader, Fetcher interface, enableLiveMode(), and the Live Content API for progressive enhancement.
- [Overlays and click-to-edit](https://www.sanity.io/docs/visual-editing/visual-editing-overlays): Enable overlays with enableVisualEditing(), understand the five content detection methods, integrate your router, and handle refreshes when content changes.
- [Build a complete visual editing integration](https://www.sanity.io/docs/visual-editing/build-a-visual-editing-integration): Build a complete framework-agnostic visual editing integration step-by-step with Vite and a Node.js HTTP server.
- [Custom overlay components and controls](https://www.sanity.io/docs/visual-editing/custom-overlay-components): Visual editing overlays can be extended with custom React components for direct in-app content editing and displaying content metadata.
- [Customizing preview header and navigation](https://www.sanity.io/docs/visual-editing/customizing-preview-header-and-navigation): Learn to customize the preview header in Sanity Studio's Presentation tool, enabling users to interact with overlays and toggle features.
- [Enabling drag and drop for Visual Editing](https://www.sanity.io/docs/visual-editing/enabling-drag-and-drop): Core concepts for enabling drag and drop functionality within the Presentation tool
- [Create Studio edit intent links](https://www.sanity.io/docs/visual-editing/studio-edit-intent-links): Learn how to construct URLs that open specific documents and fields in Sanity Studio for custom editorial interfaces and preview environments.
- [Presentation Resolver API](https://www.sanity.io/docs/visual-editing/presentation-resolver-api): Programatically generate shortcuts from document forms to relevant routes in the Presentation tool
- [useOptimistic](https://www.sanity.io/docs/visual-editing/useoptimistic-reference): Instantly update UI with mutation results created directly in an application whilst awaiting updated content from Content Lake.
- [Content Source Maps](https://www.sanity.io/docs/visual-editing/content-source-maps): Content source maps allow tools to annotate content with metadata and use it to connect tools to content.
- [Vercel protection bypass](https://www.sanity.io/docs/visual-editing/vercel-protection-bypass): Bypass protection for automation is a Vercel feature for bypassing authenticated deployments. It requires additional setup to use with Presentation and Studio.
- [Troubleshooting Visual Editing](https://www.sanity.io/docs/visual-editing/troubleshooting-visual-editing)

### Use Sanity with Astro

- [Integrate Sanity with your Astro app](https://www.sanity.io/docs/astro): Astro and Sanity pair to offer fast static pages, visual editing, and the flexibility to build with components from a variety of frameworks.
- [Sanity and Astro](https://www.sanity.io/docs/astro/introduction): Build content-driven Astro websites with Sanity. Covers the @sanity/astro integration, Visual Editing, Portable Text, image handling, and starter resources.
- [Configuring @sanity/astro](https://www.sanity.io/docs/astro/configure-sanity-astro): Reference for Sanity integration configuration in Astro. Covers integration options, the sanity:client virtual module, environment variables, and more.
- [Embedding Sanity Studio in Astro](https://www.sanity.io/docs/astro/embedding-studio-in-astro): Mount Sanity Studio as a route in your Astro application. Covers studioBasePath configuration, CORS setup, multiple workspaces, and known issues.
- [Querying content in Astro](https://www.sanity.io/docs/astro/query-content-astro): Fetch Sanity content in Astro with GROQ queries. Covers basic fetching, dynamic routes, TypeGen, parameterized queries, and the loadQuery helper
- [Images and Portable Text in Astro](https://www.sanity.io/docs/astro/images-and-portable-text-astro): Render Sanity images with @sanity/image-url and rich text with astro-portabletext in your Astro components.
- [Static and server rendering in Astro](https://www.sanity.io/docs/astro/static-and-server-rendering): Choose the right rendering mode for your Astro + Sanity project.
- [Visual Editing with Astro](https://www.sanity.io/docs/visual-editing/astro-visual-editing): Configure Sanity’s Presentation Tool, draft mode, and visual editing overlays to work with an Astro 6 server-rendered frontend.

### CLI reference

- [Sanity CLI](https://www.sanity.io/docs/cli-overview): The sanity Command Line Interface (CLI) is a tool for interacting with the Sanity ecosystem from your terminal.
- [CLI Configuration](https://www.sanity.io/docs/cli-reference/cli-config): Wrangle datasets and webhooks, initialise plugin boilerplate code, build and deploy—all from the command line
- [Backups CLI command reference](https://www.sanity.io/docs/cli-reference/cli-backups): Reference documentation for the sanity backups CLI command.
- [Blueprints CLI command reference](https://www.sanity.io/docs/cli-reference/cli-blueprints): Reference documentation for the Sanity CLI Blueprints command.
- [Build CLI command reference](https://www.sanity.io/docs/cli-reference/build): Builds the current Sanity configuration to a static bundle.
- [Codemod CLI command reference](https://www.sanity.io/docs/cli-reference/codemod): Runs a code modification script
- [CORS CLI command reference](https://www.sanity.io/docs/cli-reference/cors-in-cli): Interact with CORS-entries for your project
- [Datasets CLI command reference](https://www.sanity.io/docs/cli-reference/cli-datasets): Interact with datasets in your project
- [Debug CLI command reference](https://www.sanity.io/docs/cli-reference/debug): Gathers information about your local Sanity environment.
- [Deploy CLI command reference](https://www.sanity.io/docs/cli-reference/deploy): Deploys a statically built Sanity studio
- [Dev CLI command reference](https://www.sanity.io/docs/cli-reference/dev): Starts a development server for the Sanity Studio
- [Docs CLI command reference](https://www.sanity.io/docs/cli-reference/docs): Browse, read, and search the Sanity documentation from the CLI.
- [Documents CLI command reference](https://www.sanity.io/docs/cli-reference/documents): Interact with documents in your project
- [Exec CLI command reference](https://www.sanity.io/docs/cli-reference/exec): Runs a script in Sanity context
- [Functions CLI command reference](https://www.sanity.io/docs/cli-reference/functions): Interact with and test your Sanity Functions from the CLI.
- [GraphQL CLI command reference](https://www.sanity.io/docs/cli-reference/cli-graphql): Deploy, delete and list GraphQL APIs for Sanity projects
- [Help CLI command reference](https://www.sanity.io/docs/cli-reference/help): Displays help information about Sanity
- [Hooks CLI command reference](https://www.sanity.io/docs/cli-reference/cli-hooks): Interact with hooks in your project
- [Init CLI command reference](https://www.sanity.io/docs/cli-reference/init): Initialize a new Sanity project or plugin
- [Install CLI command reference](https://www.sanity.io/docs/cli-reference/install): Installs dependencies of the current project
- [Learn CLI command reference](https://www.sanity.io/docs/cli-reference/cli-learn): Reference documentation for the Sanity CLI learn command.
- [Login CLI command reference](https://www.sanity.io/docs/cli-reference/login): Authenticates against the Sanity.io API or a third-party identity provider via SAML SSO (Business / Enterprise plan feature).
- [Logout CLI command reference](https://www.sanity.io/docs/cli-reference/logout): Logs out of the Sanity.io session
- [Manage CLI command reference](https://www.sanity.io/docs/cli-reference/manage): Opens the Sanity project management UI
- [Manifest CLI command reference](https://www.sanity.io/docs/cli-reference/manifest): Extracts a JSON manifest for use with Sanity Canvas.
- [MCP CLI command reference](https://www.sanity.io/docs/cli-reference/cli-mcp): Reference documentation for the Sanity CLI mcp command.
- [Media CLI command reference](https://www.sanity.io/docs/cli-reference/media): CLI reference documentation for the media command.
- [Migrations CLI command reference](https://www.sanity.io/docs/cli-reference/cli-migrations): Create, list, and run content migrations
- [OpenAPI CLI command reference](https://www.sanity.io/docs/cli-reference/openapi): Command group with list and get subcommands for accessing Sanity OpenAPI specifications directly from the CLI.
- [Preview CLI command reference](https://www.sanity.io/docs/cli-reference/preview): Starts a local web server for previewing production build
- [Projects CLI command reference](https://www.sanity.io/docs/cli-reference/projects): Get information about projects for your logged in user
- [Schemas CLI command reference](https://www.sanity.io/docs/cli-reference/cli-schemas): List, validate, extract, and deploy schema.
- [Start CLI command reference](https://www.sanity.io/docs/cli-reference/start): Alias of `sanity preview`
- [Telemetry CLI command reference](https://www.sanity.io/docs/cli-reference/telemetry): Interact with telemetry settings for your logged in user
- [TypeGen CLI command reference](https://www.sanity.io/docs/cli-reference/cli-typegen): Generate TypeScript type definition from a Studio schema and GROQ queries
- [Undeploy CLI command reference](https://www.sanity.io/docs/cli-reference/undeploy): Removes the deployed studio from <your-studio-name>.sanity.studio.
- [Users CLI command reference](https://www.sanity.io/docs/cli-reference/users): Manage users of your project
- [Versions CLI command reference](https://www.sanity.io/docs/cli-reference/versions): Shows the installed versions of Sanity CLI and core components
- [Tokens CLI command reference](https://www.sanity.io/docs/cli-reference/tokens): Create, inspect and manage tokens

### Content Lake (Datastore)

- [Store and query structured content](https://www.sanity.io/docs/content-lake): Sanity's Content Lake stores your content as structured data, making it queryable, referenceable, and ready for delivery to any channel.
- [Technical limits](https://www.sanity.io/docs/content-lake/technical-limits): A list of data store limits.
- [API Versioning](https://www.sanity.io/docs/content-lake/api-versioning): How to handle versioning in the Sanity API
- [API CDN](https://www.sanity.io/docs/content-lake/api-cdn): Description of the CDN-distributed, cached version of the Sanity API.
- [Datasets](https://www.sanity.io/docs/content-lake/datasets): Managing multiple datasets within a project
- [Documents](https://www.sanity.io/docs/content-lake/documents): Sanity stores your data, and some system data, in JSON documents.
- [Drafts](https://www.sanity.io/docs/content-lake/drafts): How drafts work, and how you disable them
- [IDs and paths](https://www.sanity.io/docs/content-lake/ids): How document IDs work, and what you can do with them
- [Perspectives for Content Lake](https://www.sanity.io/docs/content-lake/perspectives): Perform the same query but with different results based on the published or draft status of a document.
- [Attribute limit](https://www.sanity.io/docs/content-lake/attribute-limit): Everything about the attribute limit: what it is, how to avoid it, and what to do if you hit the limit on one of your projects.
- [How to use Hot Swapping for datasets](https://www.sanity.io/docs/content-lake/how-to-use-hot-swapping-for-datasets): Use aliases to swap datasets with no migrations or code changes
- [How to use Cloud Clone for datasets](https://www.sanity.io/docs/content-lake/how-to-use-cloud-clone-for-datasets): Copy a dataset inside Sanity's infrastructure using either the CLI or HTTP API.
- [Backups](https://www.sanity.io/docs/content-lake/backups): Sanity offers a backup feature for data recovery and auditing, available for enterprise plans, managed via Sanity CLI.
- [Dataset Embeddings](https://www.sanity.io/docs/content-lake/dataset-embeddings): Search your Content Lake by meaning, not just keywords.
- [Hierarchy](https://www.sanity.io/docs/content-lake/hierarchy): Sanity’s hierarchy primitive lets you organise documents into a tree, similar to a file system.
- [GROQ introduction](https://www.sanity.io/docs/content-lake/groq-introduction): GROQ (Graph-Relational Object Queries) is Sanity's powerful query language designed to help you describe exactly what information your application needs.
- [How GROQ queries work](https://www.sanity.io/docs/content-lake/how-queries-work): A tutorial on using the Sanity query language GROQ.
- [Custom GROQ functions](https://www.sanity.io/docs/content-lake/custom-groq-functions): Learn how to create your own GROQ functions.
- [GROQ query cheat sheet](https://www.sanity.io/docs/content-lake/query-cheat-sheet): Data query examples.
- [Search text content with GROQ](https://www.sanity.io/docs/content-lake/search-content-with-groq): A guide to searching Sanity text content using GROQ, from basic text matching to advanced hybrid search that combines keyword and semantic strategies.
- [The Vision plugin](https://www.sanity.io/docs/content-lake/the-vision-plugin): Quickly test your GROQ queries using this studio plugin.
- [GROQ syntax](https://www.sanity.io/docs/specifications/groq-syntax): Reference documentation for the GROQ syntax.
- [GROQ feature support across Sanity](https://www.sanity.io/docs/content-lake/groq-feature-support-by-context): A summary of GROQ language support and limitations across different Sanity contexts.
- [GraphQL](https://www.sanity.io/docs/content-lake/graphql): How to deploy and query GraphQL API for your Sanity projects
- [GROQ for GraphQL developers](https://www.sanity.io/docs/content-lake/what-about-graphql): Why don't we use GraphQL as our primary query language, and what to do if you want a GraphQL API on your data
- [Introduction to document mutations](https://www.sanity.io/docs/content-lake/mutations-introduction): Sanity's Content Lake offers a variety of methods for creating, editing, and deleting documents.
- [Mutate documents with actions](https://www.sanity.io/docs/content-lake/dispatch-actions): The Actions API let you use the same system Sanity Studio uses to mutate documents in Content Lake.
- [Transactions](https://www.sanity.io/docs/content-lake/transactions): How transactions for Content Lake work
- [Patches](https://www.sanity.io/docs/content-lake/http-patches): The valid patch types when using the direct HTTP mutations api.
- [Document mutation patterns](https://www.sanity.io/docs/content-lake/mutation-patterns): Common patterns and snippets for mutating documents and data in the Sanity Content Lake.
- [Assets](https://www.sanity.io/docs/content-lake/assets): Sanity provides extensible UI for managing assets, and an API for dealing with storage, resizing and deletion.
- [Upload, query, and delete assets](https://www.sanity.io/docs/content-lake/manage-assets): Programmatically manage assets in your project dataset.
- [Image Metadata](https://www.sanity.io/docs/apis-and-sdks/image-metadata): This article takes a closer look at the types of metadata available for images, and the values they might return.
- [Image transformations](https://www.sanity.io/docs/apis-and-sdks/image-urls): Reference documentation for image transformations.
- [International Image Interoperability Framework (IIIF) API reference](https://www.sanity.io/docs/apis-and-sdks/iiif-api-reference): The International Image Interoperability Framework (IIIF) provides a standardized way of delivering and describing images shared on the web. This is the reference documentation for how you can interact with the asset pipeline using IIIF.
- [Importing data](https://www.sanity.io/docs/content-lake/importing-data): How to go about importing data in bulk, including file and image assets.
- [Restore a deleted dataset from a backup](https://www.sanity.io/docs/content-lake/restore-deleted-dataset): Use an backup to restore a deleted dataset.
- [Migrating your schema and content](https://www.sanity.io/docs/content-lake/schema-and-content-migrations): How to migrate schema and content within a Sanity project
- [Content migration cheat sheet](https://www.sanity.io/docs/content-lake/content-migration-cheatsheet): Common content migration patterns that can be run by the Sanity CLI
- [Important considerations for schema and content migrations](https://www.sanity.io/docs/content-lake/important-considerations-for-schema-and-content-migrations): How to derisk changes to your schema and plan for successful content migrations
- [Schema validation and the Content Lake](https://www.sanity.io/docs/content-lake/schema-validation-and-the-content-lake): Understand why schema validation only runs in Sanity Studio and what that means when writing data through the API or client libraries.
- [Presenting and previewing content](https://www.sanity.io/docs/content-lake/presenting-and-previewing-content): Previewing changes to your content in a secure and high-fidelity setting before publishing is essential to a smooth editorial process.
- [Live Content API](https://www.sanity.io/docs/content-lake/live-content-api): Documentation for the Live Content API, which allows you to deliver live, dynamic experiences to your users without the complexity and scalability challenges.
- [Real-time updates](https://www.sanity.io/docs/content-lake/realtime-updates): How API clients can listen for data changes in realtime.
- [GROQ-powered webhooks](https://www.sanity.io/docs/content-lake/webhooks): Send custom HTTP requests when something in your content lake has changed. Use GROQ to define what should trigger a webhook and its payload.
- [Webhook Best Practices](https://www.sanity.io/docs/content-lake/webhook-best-practices): Learn best practices about configuration and handling of webhooks
- [Webhooks API reference](https://www.sanity.io/docs/http-reference/webhooks): Reference documentation for the Webhooks HTTP endpoints.
- [Embeddings index introduction](https://www.sanity.io/docs/content-lake/embeddings-index-api-overview): Embeddings allow you to search for what your documents are about. Use the Embeddings Index API to build LLM agents or to enable semantic search.
- [Create and query an embeddings index](https://www.sanity.io/docs/content-lake/create-query-embeddings-index): To get started with using the embeddings index API, you first need to create an index.
- [Embeddings Index CLI reference](https://www.sanity.io/docs/libraries/embeddings-index-cli-reference): Reference documentation of the Sanity Embeddings Index CLI to create and manage embeddings indexes for your content.
- [Embeddings Index API reference](https://www.sanity.io/docs/http-reference/embeddings-index): Reference documentation for the Embeddings Index HTTP endpoints.
- [Access your data (CORS)](https://www.sanity.io/docs/content-lake/cors): Decide which domains can access your project data.
- [Browser security & CORS](https://www.sanity.io/docs/content-lake/browser-security-and-cors): Best security practice when using access tokens when interacting with the API.
- [Keeping your data safe](https://www.sanity.io/docs/content-lake/keeping-your-data-safe): Best practices for access token security.
- [Activity Feed](https://www.sanity.io/docs/platform-management/activity-feed)
- [Common Sanity document types](https://www.sanity.io/docs/content-lake/document-reference): Reference documentation for common Sanity document shapes.
- [Roles and permissions](https://www.sanity.io/docs/content-lake/roles-concepts): API endpoints for managing roles and permissions
- [URL format](https://www.sanity.io/docs/content-lake/http-urls): tl;dr: <projectId>.api.sanity.io/<version>/<path>
- [Authentication and tokens](https://www.sanity.io/docs/content-lake/http-auth): How to create tokens and make authenticated requests.
- [JSONMatch](https://www.sanity.io/docs/content-lake/json-match): Rich ways to address specific values in Sanity documents
- [IP addresses used by Sanity](https://www.sanity.io/docs/content-lake/ip-addresses): Reference documentation for Sanity IP address ranges.

### Next.js quick start

- [Setting up your studio](https://www.sanity.io/docs/setting-up-your-studio): Quickstart for getting up and running with Sanity from scratch.
- [Defining a schema](https://www.sanity.io/docs/defining-a-schema): The Sanity Studio can only interact with documents in a dataset for which it has schema types registered in its configuration. It currently has none.
- [Displaying content in Next.js](https://www.sanity.io/docs/next-js-quickstart/displaying-content-in-next-js): Query your content and render it in a Next.js app.
- [Deploying Studio and inviting editors](https://www.sanity.io/docs/deploying-studio-and-inviting-editors): Your Sanity Studio is still only running on your local computer. It's time to deploy and get it into the hands of other content editors.

### Platform management

- [Administer organizations, projects, datasets, and users](https://www.sanity.io/docs/platform-management): Control and configure your Sanity projects with tools for managing environments, deployment, backups, monitoring, and other operational aspects.
- [Platform terminology](https://www.sanity.io/docs/platform-management/platform-terminology): To understand how to share work among teams, familiarize yourself with core Sanity concepts that describe where the hard boundaries and connected features are.
- [Plans and payments](https://www.sanity.io/docs/platform-management/plans-and-payments): Learn how billing and quotas work for different plans.
- [Projects, organizations, and billing](https://www.sanity.io/docs/platform-management/projects-organizations-and-billing): How to create, manage, and delete organizations.
- [Understanding the Growth plan trial](https://www.sanity.io/docs/platform-management/growth-plan-trial): The Growth plan trial lets you experience more of Sanity's additional capabilities for free for a limited period of time.
- [Extending the Growth plan with paid add-ons](https://www.sanity.io/docs/platform-management/growth-plan-add-ons): Add-ons lets you customize your Growth plan project further with enterprise-grade à la carte features.
- [Sanity's non-profit plan](https://www.sanity.io/docs/platform-management/non-profit-plan): Sanity offers a heavily discounted non-profit plan for eligible non-profit organizations.
- [How AI Credits work](https://www.sanity.io/docs/platform-management/how-ai-credits-work): Understand how AI credits are consumed and billed for Sanity AI tooling.
- [Activity Feed](https://www.sanity.io/docs/platform-management/activity-feed)
- [Request logs](https://www.sanity.io/docs/platform-management/request-logs): Learn how to set up Sanity to deliver detailed logs for API requests, enabling insights into content interaction and bandwidth usage.
- [Request tags](https://www.sanity.io/docs/platform-management/reference-api-request-tags): Request tags in Sanity Log Delivery can be added to API and CDN requests for filtering and aggregating log data, supported by @sanity/client.
- [Request logs data reference](https://www.sanity.io/docs/platform-management/reference-request-log-data): The article explains the file format and data structure of the API request log feature, detailing the content and available data.

### User guides

- [User Guides](https://www.sanity.io/docs/user-guide): Practical, easy-to-follow guides that help content teams work efficiently across official Sanity applications.
- [Meet the Dashboard](https://www.sanity.io/docs/dashboard/dashboard-introduction): The central hub for all your content operations.
- [Content operators quick start guide](https://www.sanity.io/docs/user-guides/content-operations-cheatsheet): Practical tips and instructions for managing your content within the Sanity ecosystem
- [Comments for Sanity Studio](https://www.sanity.io/docs/studio/comments): Learn to use Comments in Sanity Studio for effective collaboration, including leaving comments, @mentions, and resolving comments.
- [Tasks for Sanity Studio](https://www.sanity.io/docs/studio/tasks): Learn to use Sanity Studio's tasks for collaboration, assign tasks, comment on tasks, and resolve tasks for efficient content creation.
- [Copy and paste fields](https://www.sanity.io/docs/user-guides/field-copy-and-paste): How to copy and paste fields and documents within your Sanity Studio.
- [Preview and page building](https://www.sanity.io/docs/visual-editing/preview-and-page-building): The Presentation tool in Sanity Studio provides a powerful visual editing experience for content creators.
- [Content Releases user guide](https://www.sanity.io/docs/user-guides/content-releases): Learn to use Content Releases to organize and schedule updates across multiple documents.
- [Compare document versions](https://www.sanity.io/docs/studio/compare-document-versions): The document comparison view in Sanity Studio provides a side-by-side view of different document versions.
- [History experience](https://www.sanity.io/docs/user-guides/history-experience): Understanding retention time, and document history status
- [Create and run instructions with AI Assist](https://www.sanity.io/docs/user-guides/ai-assist-working-with-instructions): How to create, run, and work with instructions for Sanity AI Assist.
- [Common instructions for AI Assist](https://www.sanity.io/docs/user-guides/ai-assist-cheat-sheet): Instruction cheat sheet with common tasks that can be adopted to your specific use case.
- [Media Library quick start guide](https://www.sanity.io/docs/user-guides/media-library-user-cheatsheet): Practical tips and instructions for managing your media assets within the Sanity ecosystem
- [Meet the library](https://www.sanity.io/docs/media-library/interface): Get to know Media Library's user interface.
- [Introduction to Canvas](https://www.sanity.io/docs/canvas/canvas-user-guide): Canvas is a writing tool that empowers content creation with AI assistance and contextual notes. Craft informed, engaging content effortlessly.
- [Content mapping for Canvas](https://www.sanity.io/docs/canvas/canvas-content-mapping): Bridge the gap between Canvas and Studio with content mapping
- [Roles](https://www.sanity.io/docs/user-guides/roles): Sanity enforces user access control with roles. Roles help control resource access to datasets and documents.
- [Content Agent quick start guide](https://www.sanity.io/docs/user-guides/content-agent-user-guide): Practical tips and instructions for managing content with the Content Agent

### Astro quick start

- [Setting up your studio](https://www.sanity.io/docs/setting-up-your-studio): Quickstart for getting up and running with Sanity from scratch.
- [Defining a schema](https://www.sanity.io/docs/defining-a-schema): The Sanity Studio can only interact with documents in a dataset for which it has schema types registered in its configuration. It currently has none.
- [Querying content with GROQ](https://www.sanity.io/docs/querying-content-with-groq): Content from Sanity is typically fetched as JSON from your hosted dataset using the GROQ query language.
- [Displaying content in an Astro front end](https://www.sanity.io/docs/astro-quickstart/displaying-content-in-an-astro-front-end): You’ve configured your Studio with a post document type and learned how to query from your hosted dataset. Before deploying the Studio, let’s query and display this content on the front-end framework of your choice.
- [Deploying Studio and inviting editors](https://www.sanity.io/docs/deploying-studio-and-inviting-editors): Your Sanity Studio is still only running on your local computer. It's time to deploy and get it into the hands of other content editors.

### Agent Actions

- [Agent Actions](https://www.sanity.io/docs/agent-actions): Agent Actions are dedicated interfaces for processing your content with AI and LLMs. Run them anywhere you can run code—in the cloud, in Studio, in migrations, and more.
- [Agent Actions introduction](https://www.sanity.io/docs/agent-actions/introduction): Get to know Agent Actions and how to start using them.
- [Operations](https://www.sanity.io/docs/agent-actions/operations): Agent Actions allow advanced control of how they create or edit documents.
- [Targets and paths](https://www.sanity.io/docs/agent-actions/targets-paths): Use target to target specific parts of a document with Agent Actions
- [Creating instructions](https://www.sanity.io/docs/agent-actions/instructions): Learn more about instructions and style guides, and how to use them.
- [Agent Actions patterns](https://www.sanity.io/docs/agent-actions/agent-action-cheatsheet): Explore common patterns across all Agent Actions
- [Enable references in Generate](https://www.sanity.io/docs/agent-actions/generate-add-references): Use references in Generate to populate fields and connect documents based on your instructions.
- [Create images with Agent Actions](https://www.sanity.io/docs/agent-actions/agent-actions-image-generation): Configure your schema for AI-assisted image generation.
- [Enable dates and datetimes in Agent Actions](https://www.sanity.io/docs/agent-actions/agent-actions-date-support): Configure instructions to write to date and datetime fields.
- [Generate quick start](https://www.sanity.io/docs/agent-actions/generate-quickstart): Get started with Generate by writing your first instructions to create and modify documents.
- [Generate cheat sheet](https://www.sanity.io/docs/agent-actions/generate-cheatsheet): Common patterns and best practices for using Generate
- [Translate quick start](https://www.sanity.io/docs/agent-actions/translate-quickstart): Learn to translate documents with Agent Actions Translate.
- [Translate cheat sheet](https://www.sanity.io/docs/agent-actions/translate-cheatsheet): Common patterns and examples for using Translate.
- [Transform quick start](https://www.sanity.io/docs/agent-actions/transform-quickstart): Get started with Transform by writing your first instructions to modify documents.
- [Transform cheat sheet](https://www.sanity.io/docs/agent-actions/transform-cheatsheet): Common patterns and techniques for using Agent Actions Transform.
- [Prompt quick start](https://www.sanity.io/docs/agent-actions/prompt-quickstart): Learn to send requests to the LLM using Agent Actions Prompt.
- [Patch quick start](https://www.sanity.io/docs/agent-actions/patch-quickstart): Make schema-aware patches with Agent Action Patch.

### Sanity Studio quick start

- [Setting up your studio](https://www.sanity.io/docs/setting-up-your-studio): Quickstart for getting up and running with Sanity from scratch.
- [Defining a schema](https://www.sanity.io/docs/defining-a-schema): The Sanity Studio can only interact with documents in a dataset for which it has schema types registered in its configuration. It currently has none.
- [Querying content with GROQ](https://www.sanity.io/docs/querying-content-with-groq): Content from Sanity is typically fetched as JSON from your hosted dataset using the GROQ query language.
- [Deploying Studio and inviting editors](https://www.sanity.io/docs/deploying-studio-and-inviting-editors): Your Sanity Studio is still only running on your local computer. It's time to deploy and get it into the hands of other content editors.

### Dashboard

- [Dashboard](https://www.sanity.io/docs/dashboard): The dashboard is your one-stop content operations hub. All your organization's studios and custom apps in one shared space.
- [Meet the Dashboard](https://www.sanity.io/docs/dashboard/dashboard-introduction): The central hub for all your content operations.
- [Set up and configure Dashboard](https://www.sanity.io/docs/dashboard/dashboard-configure): Get started with Sanity Dashboard, the central hub of all your content operations.

### Use Sanity with Next.js

- [Integrate Sanity with your Next.js app](https://www.sanity.io/docs/nextjs): Leverage the power of Next.js to serve your Sanity content.
- [Sanity and Next.js](https://www.sanity.io/docs/nextjs/introduction): Build content-driven Next.js applications with Sanity. Covers the next-sanity toolkit, real-time editing, live content, caching, and starter resources.
- [Configuring the Sanity client for Next.js](https://www.sanity.io/docs/nextjs/configure-sanity-client-nextjs): Complete reference for Sanity client configuration in Next.js, including useCdn, stega, tokens, defineLive, and per-request overrides.
- [Embedding Sanity Studio in Next.js](https://www.sanity.io/docs/nextjs/embedding-sanity-studio-in-nextjs): Mount Sanity Studio as a route in your Next.js app using NextStudio from next-sanity/studio. Auto and manual installation, metadata, and route separation.
- [Querying content in Next.js](https://www.sanity.io/docs/nextjs/query-content-nextjs): Use the next-sanity library to write typed GROQ queries with defineQuery and fetch content in App Router or Pages Router.
- [Rendering images in Next.js with next-sanity](https://www.sanity.io/docs/nextjs/next-sanity-image-component): Reference for the Image component and imageLoader exported from next-sanity/image. Wraps next/image with a Sanity CDN-aware loader.
- [Add live content to your application](https://www.sanity.io/docs/developer-guides/live-content-guide): Learn to use the Live Content API with Next.js or your own integration for real-time content updates in your app.
- [Caching and revalidation in Next.js](https://www.sanity.io/docs/nextjs/caching-and-revalidation-in-nextjs): Manual caching strategies for Next.js + Sanity apps, including time-based, tag-based, and path-based revalidation with the sanityFetch helper.
- [Sanity Live with Next.js Cache Components](https://www.sanity.io/docs/nextjs/cache-components): Configure next-sanity v13 for Next.js Cache Components (cacheComponents: true). Covers the three-layer component pattern, defineLive setup, draft mode handling, and manual migration from earlier versions.
- [Validating Sanity webhooks in Next.js](https://www.sanity.io/docs/nextjs/validating-sanity-webhooks-nextjs): Set up webhook-based cache revalidation in Next.js using parseBody from next-sanity/webhook. Path-based and tag-based patterns for App Router and Pages Router.
- [Visual Editing with Next.js App Router](https://www.sanity.io/docs/visual-editing/visual-editing-with-next-js-app-router): Set up visual editing between Sanity Studio and a Next.js App Router frontend, including the Sanity client, Draft Mode, Visual Editing, and Live Content.
- [Visual Editing with Next.js Pages Router](https://www.sanity.io/docs/visual-editing/visual-editing-with-next-js-pages-router): Get started with Sanity Visual Editing in a new or existing Next.js application using the Pages Router.

### Nuxt.js quick start

- [Setting up your studio](https://www.sanity.io/docs/setting-up-your-studio): Quickstart for getting up and running with Sanity from scratch.
- [Defining a schema](https://www.sanity.io/docs/defining-a-schema): The Sanity Studio can only interact with documents in a dataset for which it has schema types registered in its configuration. It currently has none.
- [Querying content with GROQ](https://www.sanity.io/docs/querying-content-with-groq): Content from Sanity is typically fetched as JSON from your hosted dataset using the GROQ query language.
- [Displaying content in a Nuxt.js front end](https://www.sanity.io/docs/nuxt-js-quickstart/displaying-content-in-nuxt-js): You’ve configured your Studio with a post document type and learned how to query from your hosted dataset. Before deploying the Studio, let’s query and display this content on the front-end framework of your choice.
- [Deploying Studio and inviting editors](https://www.sanity.io/docs/deploying-studio-and-inviting-editors): Your Sanity Studio is still only running on your local computer. It's time to deploy and get it into the hands of other content editors.

### APIs and SDKs

- [APIs and SDKs](https://www.sanity.io/docs/apis-and-sdks): Build and manage the Sanity Operating System programmatically through our APIs and SDKs. Here you find documentation for functionality that sits on top of and outside of Content Lake (our datastore) and Compute and AI layers.
- [Introduction to schemas](https://www.sanity.io/docs/apis-and-sdks/introduction-to-schemas): Learn how schemas define content structure across Sanity and design effective, evolving content models that grow with your business needs.
- [Naming things](https://www.sanity.io/docs/apis-and-sdks/naming-things): Requirements and suggestions for naming documents and fields
- [Attribute limit](https://www.sanity.io/docs/content-lake/attribute-limit): Everything about the attribute limit: what it is, how to avoid it, and what to do if you hit the limit on one of your projects.
- [Schema](https://www.sanity.io/docs/studio/schema-types): A schema describes the types of documents and fields editors may author in a Sanity Studio workspace.
- [Schema Deployment](https://www.sanity.io/docs/apis-and-sdks/schema-deployment): Deploy your schema into your dataset to enable deep integration between your content model and Sanity apps.
- [Create an aspect](https://www.sanity.io/docs/media-library/create-aspect): Create and deploy aspects for Media Library.
- [Getting started with @sanity/client](https://www.sanity.io/docs/apis-and-sdks/js-client-getting-started): Learn how to install and configure the official Sanity JavaScript client for querying and mutating content across different environments.
- [Querying content with @sanity/client](https://www.sanity.io/docs/apis-and-sdks/js-client-querying): Learn how to fetch content from your Sanity dataset using GROQ queries, perspectives, and document lookup methods with @sanity/client.
- [Creating and updating documents with @sanity/client](https://www.sanity.io/docs/apis-and-sdks/js-client-mutations): Learn how to create, update, and patch documents with @sanity/client, including array manipulation, chained operations, and conditional updates.
- [Working with assets in @sanity/client](https://www.sanity.io/docs/apis-and-sdks/js-client-assets): Learn how to upload, query, and delete assets in both Content Lake and Media Library using the Sanity JavaScript client.
- [Creating transactions with @sanity/client](https://www.sanity.io/docs/apis-and-sdks/js-client-transactions): Learn how to group multiple mutations into atomic transactions using @sanity/client, including chaining operations, inline patches, and clientless patterns.
- [Deleting documents with @sanity/client](https://www.sanity.io/docs/apis-and-sdks/js-client-deleting): Learn how to delete documents by ID or by query using the Sanity JavaScript client.
- [Content releases and versions with @sanity/client](https://www.sanity.io/docs/apis-and-sdks/js-client-releases): Learn how to create releases, manage document versions, and schedule publishing using the Sanity JavaScript client.
- [Listening to content updates with @sanity/client](https://www.sanity.io/docs/apis-and-sdks/js-client-realtime): Learn how to receive real-time content updates using the Sanity JavaScript client, with the Live Content API and query listeners.
- [Request tags for filtering logs in @sanity/client](https://www.sanity.io/docs/apis-and-sdks/js-client-request-tags): Learn how to use request tags to identify and filter API requests in your Sanity project's request logs for debugging and monitoring.
- [Advanced client patterns with @sanity/client](https://www.sanity.io/docs/apis-and-sdks/js-client-advanced): Learn about mutation options, request cancellation, and other advanced patterns when using the Sanity JavaScript client.
- [Command Line Interface (CLI)](https://www.sanity.io/docs/apis-and-sdks/cli): Build, deploy, init plugin boilerplate, run scripts, and wrangle datasets and webhooks, all from the command line
- [CLI authentication](https://www.sanity.io/docs/apis-and-sdks/cli-authentication): Before interacting with the Sanity CLI, you need to login.
- [Importing data](https://www.sanity.io/docs/content-lake/importing-data): How to go about importing data in bulk, including file and image assets.
- [CLI Configuration](https://www.sanity.io/docs/cli-reference/cli-config): Wrangle datasets and webhooks, initialise plugin boilerplate code, build and deploy—all from the command line
- [Backups](https://www.sanity.io/docs/content-lake/backups): Sanity offers a backup feature for data recovery and auditing, available for enterprise plans, managed via Sanity CLI.
- [Sanity TypeGen](https://www.sanity.io/docs/apis-and-sdks/sanity-typegen): How to use Sanity TypeGen tooling to generate TypeScript definitions from Sanity Studio schemas and GROQ queries.
- [Content Releases API](https://www.sanity.io/docs/apis-and-sdks/content-releases-api): Programmatically manage Content Releases with the API and clients.
- [Content Release API Cheat Sheet](https://www.sanity.io/docs/apis-and-sdks/content-releases-cheat-sheet): Query and modify Content Releases using the API
- [Presenting images](https://www.sanity.io/docs/apis-and-sdks/presenting-images): Presenting images through the Sanity image pipeline
- [Image transformations](https://www.sanity.io/docs/apis-and-sdks/image-urls): Reference documentation for image transformations.
- [Image Metadata](https://www.sanity.io/docs/apis-and-sdks/image-metadata): This article takes a closer look at the types of metadata available for images, and the values they might return.
- [International Image Interoperability Framework (IIIF) API reference](https://www.sanity.io/docs/apis-and-sdks/iiif-api-reference): The International Image Interoperability Framework (IIIF) provides a standardized way of delivering and describing images shared on the web. This is the reference documentation for how you can interact with the asset pipeline using IIIF.
- [Asset CDN](https://www.sanity.io/docs/apis-and-sdks/asset-cdn): Describes the CDN used for delivering assets
- [Sanity Connect for Shopify](https://www.sanity.io/docs/apis-and-sdks/sanity-connect-for-shopify): Setting up and configuring Sanity Connect for Shopify
- [Custom sync handlers for Sanity Connect](https://www.sanity.io/docs/developer-guides/custom-sync-handlers-for-sanity-connect)
- [Sanity Connect for Shopify - Reference](https://www.sanity.io/docs/apis-and-sdks/sanity-connect-for-shopify-reference): Reference documentation and code examples to set up and configure Sanity Connect for Shopify
- [Sanity Connect for Salesforce Commerce Cloud](https://www.sanity.io/docs/apis-and-sdks/sanity-connect-for-salesforce-commerce-cloud): Learn how to install and configure Sanity Connect for SFCC, sync your catalog into Sanity, and integrate enriched content into your storefront.
- [Sanity Connect for SFCC configuration reference](https://www.sanity.io/docs/apis-and-sdks/sanity-connect-sfcc-configuration-reference): Complete reference for configuring Sanity Connect for Salesforce Commerce Cloud, including site preferences, attribute mappings, and job parameters.
- [Content Agent API](https://www.sanity.io/docs/apis-and-sdks/content-agent-api): Build custom integrations with the Sanity Content Agent API.

### Content Agent

- [Content Agent](https://www.sanity.io/docs/content-agent): Sanity Content Agent is an AI assistant that helps you work with content across your Sanity projects—without writing code or GROQ queries.
- [Get started with Sanity Content Agent](https://www.sanity.io/docs/content-agent/introduction): Sanity Content Agent is an AI assistant that helps you work with content across your Sanity projects.
- [How AI Credits work](https://www.sanity.io/docs/platform-management/how-ai-credits-work): Understand how AI credits are consumed and billed for Sanity AI tooling.
- [Content Agent for Slack](https://www.sanity.io/docs/content-agent/content-agent-for-slack): Use the Sanity Content Agent directly in Slack. Search, create, and update content in your Sanity projects through conversation, without leaving your workspace.
- [Content Agent API](https://www.sanity.io/docs/apis-and-sdks/content-agent-api): Build custom integrations with the Sanity Content Agent API.

### App SDK

- [Build custom applications on Sanity](https://www.sanity.io/docs/app-sdk): Create tailored content applications with our App SDK, providing the tools needed to build custom interfaces and workflows on top of the Sanity platform.
- [App SDK Quickstart Guide](https://www.sanity.io/docs/app-sdk/sdk-quickstart): Get up and running quickly with the Sanity App SDK by following this step-by-step guide!
- [App SDK introduction](https://www.sanity.io/docs/app-sdk/sdk-introduction): Get a high-level intro to the Sanity Software Development Kit (SDK)
- [Installation](https://www.sanity.io/docs/app-sdk/installation-and-development): Learn how to bootstrap a new custom application using the Sanity SDK.
- [Configuration](https://www.sanity.io/docs/app-sdk/sdk-configuration): Learn how to connect your custom app to your Sanity content
- [App SDK deployment](https://www.sanity.io/docs/app-sdk/sdk-deployment): Learn how to deploy your custom application to your organization dashboard.
- [Document Handles](https://www.sanity.io/docs/app-sdk/document-handles): Document Handles are a central concept in the Sanity App SDK, and are important to understand when working with many of the SDK’s React hooks.
- [React Hooks](https://www.sanity.io/docs/app-sdk/sdk-react-hooks): Meet some of the most important hooks from the React SDK package.
- [React Suspense](https://www.sanity.io/docs/app-sdk/react-suspense-sdk): Learn how the Sanity App SDK uses established React patterns to facilitate working with live content.
- [Authentication with the App SDK](https://www.sanity.io/docs/app-sdk/sdk-authentication): Learn about the mechanisms that enable authentication when building with the App SDK.
- [App SDK best practices](https://www.sanity.io/docs/app-sdk/sdk-best-practices): Opinionated patterns and guidance for building custom apps with the Sanity App SDK
- [Fetching and handling content](https://www.sanity.io/docs/app-sdk/fetching-and-handling-content): Learn about the central concepts and hooks for pulling content from your Sanity project into your custom app.
- [Editing documents](https://www.sanity.io/docs/app-sdk/editing-documents): Explore different methods and patterns for editing documents with the App SDK.
- [Using Sanity UI with the App SDK](https://www.sanity.io/docs/app-sdk/sanity-ui-sdk): How to integrate @sanity/ui, or any other UI library, in your app.
- [Using Tailwind with the App SDK](https://www.sanity.io/docs/app-sdk/tailwind-sdk): Learn how to use Tailwind in your custom apps built on Sanity, powered by the App SDK.
- [App SDK and TypeGen](https://www.sanity.io/docs/app-sdk/sdk-typegen): Learn how to use Sanity TypeGen with the App SDK for increased type safety and improved developer experience.

### Studio

- [Studio](https://www.sanity.io/docs/sanity-studio): Sanity Studio is an open-source, real-time collaborative content workbench where developers define content models using JavaScript objects. The Studio automatically generates a powerful editing environment based on these definitions, while offering extensive customization options through a React-based framework to tailor the editorial experience to your specific workflows.
- [Installation](https://www.sanity.io/docs/studio/installation): How to install and initiate a new Sanity Studio project
- [Studio project structure](https://www.sanity.io/docs/studio/project-structure): The file structure of a typical Sanity Studio project
- [Studio development](https://www.sanity.io/docs/studio/development): Learn how the default local development environment for Sanity Studio works
- [Hosting and deployment](https://www.sanity.io/docs/studio/deployment): How to deploy Sanity Studio, either on your own or using our hosted service.
- [Embedding Sanity Studio](https://www.sanity.io/docs/studio/embedding-sanity-studio)
- [Upgrading Sanity Studio](https://www.sanity.io/docs/studio/upgrade): How to upgrade Sanity Studio
- [Environment Variables](https://www.sanity.io/docs/studio/environment-variables): You can use environment variables to dynamically configure the Studio depending on what context it‘s in.
- [Using TypeScript in Sanity Studio](https://www.sanity.io/docs/studio/using-typescript-in-sanity-studio): How to use TypeScript with Sanity Studio
- [Understanding the latest version of Sanity](https://www.sanity.io/docs/studio/latest-version-of-sanity): Learn about the latest features and improvements in the newest version of Sanity.
- [System requirements](https://www.sanity.io/docs/studio/system-requirements): Network, browser, and infrastructure requirements for running Sanity Studio in managed environments.
- [Configuration](https://www.sanity.io/docs/studio/configuration): Sanity Studio lets you quickly get up and running by configuring it with simple JavaScript or TypeScript.
- [Workspaces](https://www.sanity.io/docs/studio/workspaces): Learn about working with multiple workspaces within a single studio setup
- [Schemas and Forms](https://www.sanity.io/docs/studio/schemas-and-forms): Schemas are the main mechanism for describing your content and how to interact with it in the studio.
- [Conditional fields](https://www.sanity.io/docs/studio/conditional-fields): How to make field visibility conditional, based on other fields' values or on information about the current user.
- [Field Groups](https://www.sanity.io/docs/studio/field-groups): Organize your content editing experience by grouping fields together under tabs.
- [List previews](https://www.sanity.io/docs/studio/previews-list-views): Configure and customize how documents are displayed within Sanity Studio's document lists.
- [Connected Content](https://www.sanity.io/docs/studio/connected-content): Structured content is connected. It's what enables reusing and repurposing the same chunk of content in different contexts, and it's how you enable your content to be treated as data. The Content Lake has some unique capabilities that make connected, structured content not only possible but pleasant to work with both programmatically through APIs and in the studio. This article aims to unpack how to use and think about references. While it has some technical language and concepts, you should be able to tag along, even if you aren't super familiar with JavaScript, JSON, or GROQ, our primary query language.
- [Validation](https://www.sanity.io/docs/studio/validation): Describes how to validate documents within the content studio.
- [Initial Value Templates](https://www.sanity.io/docs/studio/initial-value-templates): Define an initial value for a new document created in Sanity Studio.
- [Cross Dataset References](https://www.sanity.io/docs/studio/cross-dataset-references): All you need to know about creating references across datasets.
- [Sort orders](https://www.sanity.io/docs/studio/sort-orders): Manage how Studio sorts documents.
- [Incoming reference decoration](https://www.sanity.io/docs/studio/incoming-reference-decoration): Display incoming references directly in a document's form, without storing the data as part of the document.
- [Block Content](https://www.sanity.io/docs/studio/block-content): Block content allows you to create a rich text experience tailored to the needs of your content.
- [Configure the Portable Text Editor](https://www.sanity.io/docs/studio/portable-text-editor-configuration): Set up and configure the Portable Text Editor with decorators, annotations, and block content.
- [Customize the Portable Text Editor](https://www.sanity.io/docs/studio/customizing-the-portable-text-editor): Customization guidelines and examples to tailor the Portable Text editor to your needs.
- [Create a Portable Text behavior plugin](https://www.sanity.io/docs/studio/pte-plugins): Use behavior plugins to add custom interactions to the Portable Text block editor in Studio.
- [Add Portable Text Editor plugins to Studio](https://www.sanity.io/docs/studio/add-portable-text-plugins): Use official and community-built Portable Text Editor plugins in your studio.
- [Common Portable Text Editor patterns](https://www.sanity.io/docs/studio/customizing-block-content): This series of practical examples shows how to customize block content and the Portable Text Editor in Sanity Studio.
- [Studio customization](https://www.sanity.io/docs/studio/studio-customization): With Studio customization, you can transform the default editing experience into one that matches your team's needs.
- [Custom component for Sanity Studio](https://www.sanity.io/docs/studio/intro-to-custom-studio-components): Change the look and feel of your studio and craft tailor-made editorial interactions.
- [Custom authentication](https://www.sanity.io/docs/studio/custom-auth): The Studio can be configured to use your own login solution rather than the standard ones by supplying the auth provider details in your studio configuration.
- [Custom asset sources](https://www.sanity.io/docs/studio/custom-asset-sources): How to add custom asset sources for Sanity Studio.
- [Introduction to Custom Diff Components](https://www.sanity.io/docs/studio/custom-diff-components): Customizing how changes between two versions of a data structure are displayed within the Sanity Studio.
- [Form Components](https://www.sanity.io/docs/studio/form-components): The Form Components API lets you customize the look and feel of the fields in your studio individually, or at a root level that will affect every field in the studio.
- [How form paths work](https://www.sanity.io/docs/studio/how-form-paths-work): Learn more about form paths, their structure, and their role as unique references to specific values in Sanity documents.
- [Icons](https://www.sanity.io/docs/studio/icons-for-data-types): Use icons for types to display in the creation dialogue and when you're missing an media preview.
- [Favicons](https://www.sanity.io/docs/studio/favicons): A "favicon" appears in places such as browser tabs, URL field and browser bookmarks. Learn how to replace the default Sanity icon with your own.
- [Localizing Sanity Studio](https://www.sanity.io/docs/studio/localizing-studio-ui): Sanity Studio supports UI localization via plugins. Users can install languages, override translations, and contribute to localization.
- [New Document Options](https://www.sanity.io/docs/studio/new-document-options): Customize the new document creation experience for creators in Sanity Studio.
- [Studio Components](https://www.sanity.io/docs/studio/studio-components): The studio components API allows you to customize the UI of your Sanity Studio.
- [Studio search configuration](https://www.sanity.io/docs/studio/studio-search-config): Global search for Sanity Studio allows content search, can hide specific documents, and allows custom field weighting.
- [Focus and UI state in custom inputs](https://www.sanity.io/docs/studio/focus-and-ui-state-in-custom-inputs): Learn more about handling UI disclosure elements. Manage focus and UI state in custom UI input elements.
- [From input components to real-time safe patches](https://www.sanity.io/docs/studio/from-input-components-to-real-time-safe-patches): Learn more about real-time safe patches, with recommendations to safely sync changes between front and back ends.
- [Sanity UI](https://www.sanity.io/docs/studio/sanity-ui): Keep your custom studio elements consistent with built-in UI components.
- [Studio Tools](https://www.sanity.io/docs/studio/studio-tools): A tool is a top-level view in the Sanity Studio application that you can access through its menu bar.
- [Create a custom Studio tool](https://www.sanity.io/docs/studio/custom-studio-tool): Add bespoke functionality to Studio with a custom tool.
- [Tools cheat sheet](https://www.sanity.io/docs/studio/tools-cheat-sheet): Common code snippets to help customize the Studio tool experience.
- [Theming](https://www.sanity.io/docs/studio/theming): Learn how to customize the styling and branding of your studio
- [The Dashboard tool for Sanity Studio](https://www.sanity.io/docs/studio/dashboard): How to set up and configure the Dashboard tool for Sanity Studio
- [Installing and configuring widgets](https://www.sanity.io/docs/studio/installing-and-configuring-widgets): How to install and configure widgets for the Dashboard tool for Sanity Studio
- [Document actions](https://www.sanity.io/docs/studio/document-actions): Introduction to building custom document actions.
- [Release Actions](https://www.sanity.io/docs/studio/release-actions): Create custom actions that display alongside the default Content Release actions.
- [Custom document badges](https://www.sanity.io/docs/studio/custom-document-badges): Introduction to implementing your own document badges.
- [Localization](https://www.sanity.io/docs/studio/localization): Localization allows you to deliver your content in different languages for your users.
- [Content Releases Configuration](https://www.sanity.io/docs/studio/content-releases-configuration): Configure Content Releases in Sanity Studio
- [Enable and configure Comments](https://www.sanity.io/docs/studio/configuring-comments): Learn how to enable and configure the Comments feature in Sanity Studio.
- [Configuring Tasks](https://www.sanity.io/docs/studio/configuring-tasks): Learn how to enable, configure, and use the Tasks feature in Sanity Studio for effective team collaboration on content creation.
- [Scheduled drafts](https://www.sanity.io/docs/studio/scheduled-drafts): Scheduled drafts allows you to schedule single-document releases for a time in the future.
- [Scheduled publishing (deprecated)](https://www.sanity.io/docs/studio/scheduled-publishing): Schedule your content for future publication and organize upcoming releases – no custom tasks or serverless functions required!
- [Manage Studio notifications](https://www.sanity.io/docs/studio/studio-notifications): Manage your Sanity Studio notifications from the user account settings page.
- [Structure tool and Structure builder](https://www.sanity.io/docs/studio/structure-introduction): The Structure tool is included with Sanity Studio and allows you to customize the experience of creating, browsing, and managing documents.
- [Get started with Structure Builder API](https://www.sanity.io/docs/studio/structure-builder-introduction): This is an introduction to important concepts for the Structure Builder API.
- [Set up Structure Builder to override the default list view](https://www.sanity.io/docs/studio/set-up-structure-builder-to-override-the-default-list-view): In this article, we'll explore how to initialize Structure Builder and override the default title of the "Content" list.
- [Create a link to a single edit page in your main document type list](https://www.sanity.io/docs/studio/create-a-link-to-a-single-edit-page-in-your-main-document-type-list): In this article, we'll explore how to add a link to a single document from the main document type list.
- [Manually group items in a pane](https://www.sanity.io/docs/studio/manually-group-items-in-a-pane): In this article, we'll manually group a few singleton "site setting" documents.
- [Dynamically group list items with a GROQ filter](https://www.sanity.io/docs/studio/dynamically-group-list-items-with-a-groq-filter): In this article, we'll use the documentList() method to dynamically group documents with a GROQ filter.
- [Create custom document views with Structure Builder](https://www.sanity.io/docs/studio/create-custom-document-views-with-structure-builder): In this article, we'll look at adding a custom document view to view the JSON data for our posts.
- [Structure Builder cheat sheet](https://www.sanity.io/docs/studio/structure-builder-cheat-sheet): The Structure Builder is a powerful – but complex – set of methods. There are a few commonly used methods which you are likely to need in your projects, and they are presented here in quick copy-and-paste friendly form.
- [Structure tool](https://www.sanity.io/docs/studio/structure-tool): Customize the document browsing and management experience in Sanity Studio with the Structure tool.
- [Structure Builder API Reference](https://www.sanity.io/docs/studio/structure-builder-reference): Overview of different methods in the Structure Builder API
- [Studio Plugins](https://www.sanity.io/docs/studio/studio-plugins): Plugins allow you to extend and customize Sanity Studio with additional functionality.
- [Installing and configuring plugins](https://www.sanity.io/docs/studio/installing-and-configuring-plugins): Learn how to extend and customize Sanity Studio with plugins.
- [Developing plugins](https://www.sanity.io/docs/studio/developing-plugins): Package plugins in a reusable and sharable way.
- [Publishing plugins](https://www.sanity.io/docs/studio/publishing-plugins): Publish a plugin for distribution
- [Internationalizing plugins](https://www.sanity.io/docs/studio/internationalizing-plugins-ui): This article provides a guide for plugin authors to add localization capabilities to their Sanity Studio plugins.
- [Plugins API](https://www.sanity.io/docs/studio/plugins-api-reference): Extend the capabilities of your studio using plugins
- [Install and configure Sanity AI Assist](https://www.sanity.io/docs/studio/install-and-configure-sanity-ai-assist): How to install and configure the AI Assist plugin for Sanity Studio.
- [Content translation with AI Assist](https://www.sanity.io/docs/studio/ai-assist-content-translation): How to set up and use AI Assist for content translations for documents and fields.
- [Custom field actions](https://www.sanity.io/docs/studio/ai-assist-field-actions): Set up and use custom field actions in AI Assist to add Agent Actions or other custom actions to the document or field action menus.
- [Field action patterns](https://www.sanity.io/docs/studio/field-actions-patterns): Examples and best practices for using AI Assist custom field actions.
- [Comments for Sanity Studio](https://www.sanity.io/docs/studio/comments): Learn to use Comments in Sanity Studio for effective collaboration, including leaving comments, @mentions, and resolving comments.
- [Tasks for Sanity Studio](https://www.sanity.io/docs/studio/tasks): Learn to use Sanity Studio's tasks for collaboration, assign tasks, comment on tasks, and resolve tasks for efficient content creation.
- [Copy and paste fields](https://www.sanity.io/docs/user-guides/field-copy-and-paste): How to copy and paste fields and documents within your Sanity Studio.
- [Compare document versions](https://www.sanity.io/docs/studio/compare-document-versions): The document comparison view in Sanity Studio provides a side-by-side view of different document versions.
- [Content Releases user guide](https://www.sanity.io/docs/user-guides/content-releases): Learn to use Content Releases to organize and schedule updates across multiple documents.
- [Scheduled drafts user guide](https://www.sanity.io/docs/studio/scheduled-drafts-user-guide): Learn to schedule individual drafts and browse scheduled drafts in the releases interface.
- [View incoming references](https://www.sanity.io/docs/studio/incoming-references): The incoming references interface displays documents that reference the active document.
- [Sanity Studio keyboard shortcuts](https://www.sanity.io/docs/studio/sanity-studio-keyboard-shortcuts): Complete reference guide to keyboard shortcuts in Sanity Studio for navigation, document editing, and tool-specific actions.
- [Schema](https://www.sanity.io/docs/studio/schema-types): A schema describes the types of documents and fields editors may author in a Sanity Studio workspace.
- [Array](https://www.sanity.io/docs/studio/array-type): Schema type for arrays of other types.
- [Block](https://www.sanity.io/docs/studio/block-type): Schema type for block which provides a rich text editor for block content.
- [Boolean](https://www.sanity.io/docs/studio/boolean-type): Schema type reference for expressing truthy values.
- [Cross Dataset Reference](https://www.sanity.io/docs/studio/cross-dataset-reference-type): A schema type for referencing documents in another dataset within the same project.
- [Date](https://www.sanity.io/docs/studio/date-type): Schema type reference for the Date type.
- [Datetime](https://www.sanity.io/docs/studio/datetime-type): The schema type for expressing an exact date and time.
- [Document](https://www.sanity.io/docs/studio/document-type): Schema type reference for expressing documents.
- [File](https://www.sanity.io/docs/studio/file-type): Schema type reference for the File type.
- [Geopoint](https://www.sanity.io/docs/studio/geopoint-type): Schema type reference for the geopoint type.
- [Global Document Reference](https://www.sanity.io/docs/studio/global-document-reference-type): Schema type reference documentation for Global Document References.
- [Image](https://www.sanity.io/docs/studio/image-type): Schema type for uploading, selecting, and editing images.
- [Number](https://www.sanity.io/docs/studio/number-type): Schema type reference for the Number type.
- [Object](https://www.sanity.io/docs/studio/object-type): Schema type to create custom types to use in a document.
- [Reference](https://www.sanity.io/docs/studio/reference-type): A schema type for referencing other documents.
- [Slug](https://www.sanity.io/docs/studio/slug-type): A schema type for slugs is typically used to create unique URLs.
- [Span](https://www.sanity.io/docs/studio/span-type): Schema type reference for the Span type.
- [String](https://www.sanity.io/docs/studio/string-type): A schema type for strings and a selectable lists of strings.
- [Text](https://www.sanity.io/docs/studio/text-type): Schema type reference for the Text type.
- [URL](https://www.sanity.io/docs/studio/url-type): Schema type reference for the URL type.
- [Asset Source API](https://www.sanity.io/docs/studio/asset-source-api-reference): As part of the Form API you can define custom asset sources for both file and image inputs.
- [Configuration API](https://www.sanity.io/docs/studio/config-api-reference): The Configuration API in Sanity Studio v3 is the primary mechanism that allows you to customize the studio.
- [Document API](https://www.sanity.io/docs/studio/document-api-reference): The document configuration API enables adding actions/badges to your studio, setting defaults for new documents, and defining a URL resolver.
- [Document Badges API](https://www.sanity.io/docs/studio/document-badges-api): Reference documentation for the document badges.
- [Document Actions reference](https://www.sanity.io/docs/studio/document-actions-api): Add custom operations to documents.
- [Form API](https://www.sanity.io/docs/studio/form-api-reference): The form API lets you customize the rendering of form components and specify options for asset sources in your studio.
- [Form Components](https://www.sanity.io/docs/studio/form-components-reference): The Form Components API will let you override default form widgets with your own custom components.
- [Studio React Hooks](https://www.sanity.io/docs/studio/studio-react-hooks): The sanity package provides utility hooks for creating custom components in your studio, with a variety of available hooks.
- [Structure Tool API](https://www.sanity.io/docs/studio/structure-tool-api): How to use the Structure Tool API to configure your structure tool(s).
- [Studio Components Reference](https://www.sanity.io/docs/studio/studio-components-reference): The Studio Components API lets you override parts of the Studio UI with custom React components.
- [Studio tools reference](https://www.sanity.io/docs/studio/tool-api-reference): A Studio Tool is a top-level view that you can access through the menu bar.
- [Initial Value Templates](https://www.sanity.io/docs/studio/initial-value-templates-api): Reference documentation for the Initial Value Templates API.

### Help articles

- [Help and troubleshooting](https://www.sanity.io/docs/help): Here you'll find articles for troubleshooting errors, migrating versions, and more.
- [Array contains multiple types that resolve to the same JSON type](https://www.sanity.io/docs/help/schema-array-of-duplicate-primitive-json-type)
- [Studio Performance Issues Caused by legacy HTTP protocols](https://www.sanity.io/docs/help/http1-performance-issues): Learn how to resolve Sanity Studio performance issues caused by outdated HTTP protocols like HTTP/1.1 by enabling HTTP/2 or 3.
- [Error: Value of type "object" is not allowed in this array field](https://www.sanity.io/docs/help/error-value-of-type-object-is-not-allowed-in-this-array-field): Error message: 
"Invalid clipboard item
Value of type "object" is not allowed in this array field"
- [AVIF](https://www.sanity.io/docs/help/avif)
- [Experimental feature: Spaces](https://www.sanity.io/docs/help/experimental-spaces)
- [Client API CDN configuration](https://www.sanity.io/docs/help/js-client-cdn-configuration)
- [Total attribute count exceeds limit](https://www.sanity.io/docs/help/3dd46662-795f-4158-be10-66e68910f6e0)
- [Desk is now Structure](https://www.sanity.io/docs/help/desk-is-now-structure): The API hitherto known as "deskTool" has been renamed "structureTool" in v3.24.1 of Sanity Studio.
- [Invalid configuration for cross dataset reference](https://www.sanity.io/docs/help/cross-dataset-reference-invalid): This help page contains links to resources on using cross dataset references.
- [Missing or duplicate context error](https://www.sanity.io/docs/help/missing-context-error): Experiencing missing or duplicate context errors in Sanity Studio? This issue often arises from having multiple versions of the sanity package installed. Learn why this happens and get tips on cleaning up dependencies or using package manager overrides to resolve the problem in our detailed guide.
- [React Compiler and Sanity](https://www.sanity.io/docs/help/react-compiler): Learn how to use the React Compiler with Sanity Studio, React 18 & 19, and for publishing Sanity plugins. Improve performance and reduce manual memoization.
- [Specify API version for studio client](https://www.sanity.io/docs/help/studio-client-specify-api-version)
- [Why give schema types a title?](https://www.sanity.io/docs/help/schema-type-title-is-recommended)
- [Array type has a invalid value for property "of"](https://www.sanity.io/docs/help/schema-array-of-invalid)
- [React 19 and Sanity](https://www.sanity.io/docs/help/react-19): Get ready to upgrade Sanity Studio and official plugins to React 19.
- [Schema: Lift anonymous object types](https://www.sanity.io/docs/help/schema-lift-anonymous-object-type)
- [Reference type has a invalid value for property "to"](https://www.sanity.io/docs/help/schema-reference-to-invalid)
- [Incorrect location for reference options](https://www.sanity.io/docs/help/schema-reference-options-nesting)
- [Invalid part syntax](https://www.sanity.io/docs/help/plugin-parts-syntax)
- [Asset metadata field](https://www.sanity.io/docs/help/asset-metadata-field-invalid)
- [Warning: userStore.currentUser is deprecated](https://www.sanity.io/docs/help/studio-user-store-currentuser-deprecated)
- [CLI errors](https://www.sanity.io/docs/help/cli-errors)
- [Renamed plugin sanity-plugin-vision](https://www.sanity.io/docs/help/renamed-plugin-vision)
- [Part name format](https://www.sanity.io/docs/help/part-name-format)
- [Array member type name is the same as a global type](https://www.sanity.io/docs/help/schema-array-of-type-global-type-conflict)
- [Changes in block schema customization properties](https://www.sanity.io/docs/help/schema-deprecated-blockeditor-key)
- [How to migrate from date to richDate](https://www.sanity.io/docs/help/migrate-to-rich-date)
- [Invalid shape of predefined choices](https://www.sanity.io/docs/help/schema-predefined-choices-invalid)
- [JS Client: Promise Polyfill](https://www.sanity.io/docs/help/js-client-promise-polyfill)
- [Introducing the document type](https://www.sanity.io/docs/help/toplevel-objects-to-document-type)
- [Unable to get a ref to an input component](https://www.sanity.io/docs/help/input-component-no-ref)
- [Outdated modules](https://www.sanity.io/docs/help/outdated-modules)
- [Upgrade studio packages](https://www.sanity.io/docs/help/upgrade-packages)
- [Block Content rendering: Image materializing](https://www.sanity.io/docs/help/block-content-image-materializing)
- [Structure: Document schema type required](https://www.sanity.io/docs/help/structure-document-type-required)
- [Parts: Declare vs implement](https://www.sanity.io/docs/help/part-declare-vs-implement)
- [Incorrect options declaration in reference](https://www.sanity.io/docs/help/schema-reference-invalid-options)
- [Block type cannot be used outside of array](https://www.sanity.io/docs/help/schema-standalone-block-type)
- [Structure: Node ID required](https://www.sanity.io/docs/help/structure-node-id-required)
- [Structure: List items must be an array](https://www.sanity.io/docs/help/structure-list-items-must-be-array)
- [Installing Node.js](https://www.sanity.io/docs/help/a5f6caba-53c9-4a9f-96ef-1bd1ae8f5c10)
- [Structure: Action or intent required](https://www.sanity.io/docs/help/structure-action-or-intent-required)
- [Object type has a invalid value for fields](https://www.sanity.io/docs/help/schema-object-fields-invalid)
- [`studioHost` and `externalStudioHost` properties deprecated](https://www.sanity.io/docs/help/studio-host-user-applications): You can deploy more than a single studio or other Sanity-powered application. Learn how to use the right API to find out where they are located.
- [Schema type is ES Module but imported through require](https://www.sanity.io/docs/help/schema-type-is-esm-module)
- [Structure: Invalid list item](https://www.sanity.io/docs/help/structure-invalid-list-item)
- [Structure: Query provided where filter is expected](https://www.sanity.io/docs/help/structure-query-provided-for-filter)
- [Structure: List item IDs must be unique](https://www.sanity.io/docs/help/structure-list-item-ids-must-be-unique)
- [Given type name is a reserved type](https://www.sanity.io/docs/help/schema-type-name-reserved)
- [Structure: Schema type not found](https://www.sanity.io/docs/help/structure-schema-type-not-found)
- [API versioning](https://www.sanity.io/docs/help/api-versioning)
- [Migrating the legacy webhook behavior to GROQ-powered Webhooks](https://www.sanity.io/docs/help/6816a33e-f07d-4fdf-ad29-14c6337e19e3)
- [Schema type is invalid](https://www.sanity.io/docs/help/schema-type-invalid)
- [Input component is missing a required prop](https://www.sanity.io/docs/help/form-builder-input-missing-required-prop)
- [Structure: Title is required](https://www.sanity.io/docs/help/structure-title-required)
- [Structure: Filter is required](https://www.sanity.io/docs/help/structure-filter-required)
- [Import: Asset file does not exist](https://www.sanity.io/docs/help/import-asset-file-does-not-exist)
- [Input component is missing a required method](https://www.sanity.io/docs/help/input-component-missing-required-method)
- [Implementing non-overridable part](https://www.sanity.io/docs/help/implement-non-overridable-part)
- [Structure: Item returned no child](https://www.sanity.io/docs/help/structure-item-returned-no-child)
- [How to migrate your block text schema for the new definition of inline objects](https://www.sanity.io/docs/help/migrate-to-block-inline-types)
- [Structure: Schema type is required](https://www.sanity.io/docs/help/structure-schema-type-required)
- [How to migrate from blocks spans to block children](https://www.sanity.io/docs/help/migrate-to-block-children)
- [Array type cannot contain array member](https://www.sanity.io/docs/help/schema-array-of-array)
- [Using tokens in the browser](https://www.sanity.io/docs/help/js-client-browser-token)
- [GraphQL](https://www.sanity.io/docs/help/graphql-beta)
- [Array member type name conflicts with built-in type](https://www.sanity.io/docs/help/schema-array-of-type-builtin-type-conflict)
- [Source vs. compiled paths](https://www.sanity.io/docs/help/source-vs-compiled-paths)
- [Import: Asset has different target than source](https://www.sanity.io/docs/help/import-asset-has-different-target)
- [Using global studio client without specifying API version](https://www.sanity.io/docs/help/studio-client-global-config)
- [Structure: Action and intent are mutually exclusive](https://www.sanity.io/docs/help/structure-action-and-intent-mutually-exclusive)
- [Upgrade React](https://www.sanity.io/docs/help/upgrade-react)
- [Plugin is missing a sanity.json file](https://www.sanity.io/docs/help/missing-plugin-sanity-json)
- [Structure: Document ID required](https://www.sanity.io/docs/help/structure-document-id-required)
- [Incompatible combination of params and filter](https://www.sanity.io/docs/help/schema-reference-filter-params-combination)
- [Using listener with tokens is not supported in browsers](https://www.sanity.io/docs/help/js-client-listener-tokens-browser)
- [Schema type is missing a required property](https://www.sanity.io/docs/help/schema-type-missing-name-or-type)
- [API versioning in Javascript Client](https://www.sanity.io/docs/help/js-client-api-version)
- [Upgrade version of studio package](https://www.sanity.io/docs/help/upgrade-package)
- [Slug: `slugifyFn` renamed](https://www.sanity.io/docs/help/slug-slugifyfn-renamed)
- [Renamed plugin @sanity/date-input](https://www.sanity.io/docs/help/deprecated-sanity-date-input)
- [Specify API version when using custom document list filters](https://www.sanity.io/docs/help/structure-api-version-required-for-custom-filter)
- [Function Timeout](https://www.sanity.io/docs/help/functions-timeout): Resolve timeout errors in Sanity Functions by adjusting the timeout duration.
- [Functions rate limit](https://www.sanity.io/docs/help/functions-rate-limit): Rate limiting helps prevent recursive functions from running indefinitely.
- [Configuring typegen in Sanity CLI config](https://www.sanity.io/docs/help/configuring-typegen-in-sanity-cli-config): As of version 4.19.0 it is recommended to configure typegen through the Sanity CLI config.
- [Studio v3 to v4](https://www.sanity.io/docs/help/v3-to-v4): Upgrading to v4 adds Node.js 20 as a requirement and requires minimal, if any, changes in your apps.
- [Email addresses show [email protection]](https://www.sanity.io/docs/help/cloudflare-email-protection): CDN security features can sometimes affect your content.
- [Next.js 16 and SanityLive: avoiding request overages](https://www.sanity.io/docs/help/nextjs-16-sanitylive-status): Upgrading to Next.js 16 with SanityLive can multiply prefetch requests and ISR writes, leading to Sanity API overages. Workarounds and what to expect.

### Developer Documentation

- [A very short introduction](https://www.sanity.io/docs/getting-started/the-sanity-content-operating-system-an-introduction): Sanity is the back-end built for AI content operations. Power web, mobile, and agentic applications at scale.

### React Router (Remix) quick start

- [Setting up your studio](https://www.sanity.io/docs/setting-up-your-studio): Quickstart for getting up and running with Sanity from scratch.
- [Defining a schema](https://www.sanity.io/docs/defining-a-schema): The Sanity Studio can only interact with documents in a dataset for which it has schema types registered in its configuration. It currently has none.
- [Querying content with GROQ](https://www.sanity.io/docs/querying-content-with-groq): Content from Sanity is typically fetched as JSON from your hosted dataset using the GROQ query language.
- [Displaying content in a React Router front end](https://www.sanity.io/docs/react-router-quickstart/displaying-content-in-a-react-router-front-end): You’ve configured your Studio with a post document type and learned how to query from your hosted dataset. Before deploying the Studio, let’s query and display this content on the front-end framework of your choice.
- [Deploying Studio and inviting editors](https://www.sanity.io/docs/deploying-studio-and-inviting-editors): Your Sanity Studio is still only running on your local computer. It's time to deploy and get it into the hands of other content editors.

### Media Library

- [Media Library](https://www.sanity.io/docs/media-library): Media Library allows teams to manage assets in a centralized place. Upload, organize, and sort—then use them across your entire organization.
- [Media Library introduction](https://www.sanity.io/docs/media-library/introduction): Learn about Media Library, how to incorporate it into your workflow, and how to get started.
- [Meet the library](https://www.sanity.io/docs/media-library/interface): Get to know Media Library's user interface.
- [Asset Versions](https://www.sanity.io/docs/media-library/asset-versions): Manage asset versions in Media Library
- [Configure Studio](https://www.sanity.io/docs/media-library/configure-studio): Enable Media Library in your Studios.
- [Configure your library](https://www.sanity.io/docs/media-library/configure-library): Set up and configure your media library
- [Create an aspect](https://www.sanity.io/docs/media-library/create-aspect): Create and deploy aspects for Media Library.
- [Add an aspect to an asset](https://www.sanity.io/docs/media-library/assign-aspects): Add aspects to an asset programmatically.
- [Query aspects](https://www.sanity.io/docs/media-library/query-aspects): Query aspects in the Media Library dataset.
- [Aspect patterns](https://www.sanity.io/docs/media-library/aspect-patterns): Common patterns for defining aspects
- [Importing assets to Media Library](https://www.sanity.io/docs/media-library/importing-assets): Import assets in bulk and automatically categorize with aspect data.
- [Upload assets programmatically](https://www.sanity.io/docs/media-library/upload-assets): Programmatically upload assets to your Media Library.
- [Folders](https://www.sanity.io/docs/media-library/folders): Organize Media Library assets into a navigable hierarchy with folders.
- [Link assets to documents](https://www.sanity.io/docs/media-library/link-media-assets): Linking an asset in the Media Library to a document in your project requires a few extra steps.
- [Asset visibility](https://www.sanity.io/docs/media-library/asset-visibility): Control asset access using visibility settings and enable secure delivery using signed URLs.
- [Container URLs ](https://www.sanity.io/docs/media-library/container-urls): Container URLs provide a stable, shareable link to Media Library assets.
- [Working with video](https://www.sanity.io/docs/media-library/working-with-video): Learn how to handle video content in Sanity's Media Library.
- [Migrate assets from Media Plugin to Media Library](https://www.sanity.io/docs/media-library/media-migration): Moving from Media Plugin to Media Library requires that you move your assets, re-link them to your documents, and update any references.
- [Media Library API reference](https://www.sanity.io/docs/http-reference/media-library): HTTP endpoints reference for the Media Library API
- [Media CLI command reference](https://www.sanity.io/docs/cli-reference/media): CLI reference documentation for the media command.
- [Media Library limits and usage details](https://www.sanity.io/docs/media-library/limits-and-usage): Technical limits and details on included usage for the media library.

### Developer guides

- [Developer guides](https://www.sanity.io/docs/developer-guides): Official implementation guides from the Sanity team
- [Get started with AI-powered Sanity development](https://www.sanity.io/docs/ai/ai-quickstart): Set up the Sanity Agent Toolkit and MCP server to help AI assistants generate high-quality Sanity code that follows established best practices.
- [Paginating with GROQ](https://www.sanity.io/docs/developer-guides/paginating-with-groq): Learn efficient pagination in GROQ using cursor-based filtering instead of array slicing. Covers tiebreakers for non-unique fields and batch processing.
- [High performance GROQ](https://www.sanity.io/docs/developer-guides/high-performance-groq)
- [Setting up Single Sign-On with SAML](https://www.sanity.io/docs/developer-guides/sso-saml): This article will take you through the process of setting up SAML (Security Assertion Markup Language) SSO (Single Sign-on) for your organization.
- [Third-Party Login (Deprecated)](https://www.sanity.io/docs/developer-guides/third-party-login): Describes integration with third-party authentication systems
- [Set up SSO authentication with SAML and Azure/Entra ID](https://www.sanity.io/docs/developer-guides/set-up-sso-authentication-with-saml-and-azure): Implement single sign-on authentication with the SAML protocol and Microsoft Azure AD/ Entra ID as the identity provider.
- [Set up SSO authentication with SAML and PingIdentity](https://www.sanity.io/docs/developer-guides/set-up-sso-authentication-with-saml-and-pingidentity): Implement single-sign on for Sanity with PingIdentity SAML
- [Set up SSO authentication with SAML and JumpCloud](https://www.sanity.io/docs/developer-guides/set-up-sso-authentication-with-saml-and-jumpcloud): Implement single-sign on for Sanity with JumpCloud
- [Reconcile users against internal systems](https://www.sanity.io/docs/developer-guides/remove-project-users-in-bulk): Use Sanity API's to compare current project members against an internal list to remove those that no longer require access
- [Restrict Access to Specific Documents](https://www.sanity.io/docs/developer-guides/restrict-access-to-specific-documents): Create document level access controls with Sanity
- [Setting up a Default Relay State for IdP Initiated - SAML Logins](https://www.sanity.io/docs/developer-guides/setting-up-a-default-relay-state-for-idp-initiated-saml-logins): Add a default landing url for users logging in through SSO
- [Scalable navigation patterns](https://www.sanity.io/docs/developer-guides/navigation-with-sanity): Build scalable navigation in Sanity—from simple menus to mega menus—with best practices for structure and dynamic links.
- [An opinionated guide to Sanity Studio](https://www.sanity.io/docs/developer-guides/an-opinionated-guide-to-sanity-studio): Sanity Studio is an incredibly flexible tool with near limitless customisation. Here's how I use it.
- [Browsing Content How You Want with Structure Builder](https://www.sanity.io/docs/developer-guides/getting-started-with-structure-builder): How to make content more browseable using the Structure Builder API for Sanity Studio‘s Desk Tool
- [Deciding on fields and relationships](https://www.sanity.io/docs/developer-guides/deciding-fields-and-relationships): How to work through tricky content questions and build structures that will stand the test of time.
- [Create richer array item previews](https://www.sanity.io/docs/developer-guides/create-richer-array-item-previews): Object types use a preview property to display contextual information about an item when they are inside of an array; customizing the preview component can make them even more useful for content creators.
- [Dynamic folder structure using the currentUser and workflow states](https://www.sanity.io/docs/developer-guides/dynamic-folder-structure-using-the-currentuser-and-workflow-states): In this guide you will learn how to setup such a listener-based structure and also how to combine the results with the workflow plugin metadata.
- [Create a time duration object field](https://www.sanity.io/docs/developer-guides/create-a-time-duration-object-field): Delight your content creators with intelligent inputs for more complex data structures
- [Level up Your Edit Modal with Next/Previous Navigation Buttons for Array Items](https://www.sanity.io/docs/developer-guides/level-up-your-edit-modal-with-next-previous-navigation-buttons-for-array-items): Streamline your array edit workflow by enabling smooth navigation through array items within the default edit modal. This guide walks you through building a clean, user-friendly solution for your Sanity Studio.
- [Create a “coupon generator” string field input](https://www.sanity.io/docs/developer-guides/create-a-coupon-generator-string-field-input): Take the guesswork out of creating fields with correct values and automate content creation for authors.
- [Managing redirects with Sanity](https://www.sanity.io/docs/developer-guides/managing-redirects-with-sanity): How to use Sanity to control redirects in your JavaScript framework of choice.
- [Create a document form progress component](https://www.sanity.io/docs/developer-guides/create-a-document-progress-root-level-component): Summarise form progression by decorating the entire editing form for a document with a component loaded at the root level.
- [Create an array input field with selectable templates](https://www.sanity.io/docs/developer-guides/create-an-array-input-field-with-selectable-templates): Make repetitive content creation tasks a breeze by supplying content creators with buttons to populate complex fields.
- [Creating a Parent/Child Taxonomy](https://www.sanity.io/docs/developer-guides/parent-child-taxonomy): Create common taxonomy schemas like Categories and Tags with parent/child relationships
- [Create interactive array items for featured elements](https://www.sanity.io/docs/developer-guides/create-interactive-array-items-for-featured-elements): Save time going in-and-out of modals by moving some light interactivity to array items.
- [Create a visual string selector field input](https://www.sanity.io/docs/developer-guides/create-a-rich-string-selector-field-input): Go beyond a plain radio list of inputs by giving authors more contextually useful buttons to select values from.
- [Create a survey rating number field input](https://www.sanity.io/docs/developer-guides/create-a-survey-rating-number-field-input): Give content creators quick access to valid values by replacing the default number field input with a list of options.
- [How to use structured content for page building](https://www.sanity.io/docs/developer-guides/how-to-use-structured-content-for-page-building): Learn how to create a page builder from structured content that can withstand the test of time and redesigns.
- [Create a recycling bin for deleted documents via Sanity Functions](https://www.sanity.io/docs/developer-guides/bin-for-restoring-deleted-documents): Help your editors restore deleted documents in a dataset using Sanity Functions and a singleton bin document type.
- [Add live content to your application](https://www.sanity.io/docs/developer-guides/live-content-guide): Learn to use the Live Content API with Next.js or your own integration for real-time content updates in your app.
- [Forms with Sanity](https://www.sanity.io/docs/developer-guides/forms-with-sanity): Common approaches for using forms with Sanity
- [Vercel Integration](https://www.sanity.io/docs/developer-guides/vercel-integration): How to install and use the Sanity's official Vercel integration
- [Build your blog with Astro and Sanity](https://www.sanity.io/docs/developer-guides/sanity-astro-blog): A complete guide to setting up your blog using Astro and Sanity
- [How to implement front-end search with Sanity](https://www.sanity.io/docs/developer-guides/how-to-implement-front-end-search-with-sanity): By integrating Sanity's structured content with Algolia, you can provide your users with fast, relevant search results
- [Displaying Sanity content in Shopify](https://www.sanity.io/docs/developer-guides/displaying-sanity-content-in-shopify)
- [Sanity Connect for Shopify](https://www.sanity.io/docs/apis-and-sdks/sanity-connect-for-shopify): Setting up and configuring Sanity Connect for Shopify
- [Custom sync handlers for Sanity Connect](https://www.sanity.io/docs/developer-guides/custom-sync-handlers-for-sanity-connect)
- [Cookie consent integrations with Sanity](https://www.sanity.io/docs/developer-guides/cookie-consent-integrations-with-sanity): How to integrate a cookie consent banner with your Sanity-powered website
- [Integrating external data sources with Sanity](https://www.sanity.io/docs/developer-guides/integrating-external-data): Learn the 2 most common patterns for integrating external data sources with Sanity
- [Build email marketing campaigns with Sanity and Klaviyo](https://www.sanity.io/docs/developer-guides/email-marketing-campaigns-powered-by-sanity-functions-and-klaviyo): Learn how to use Functions to stage and send email campaigns from Sanity through Klaviyo.
- [Developing with Next.js on GitHub Codespaces ](https://www.sanity.io/docs/developer-guides/developing-with-next-js-on-github-codespaces): A guide covering step-by-step instructions for developing Next.js applications with Sanity Studio Live Preview on GitHub Codespaces.
- [Add analytics to Sanity Studio](https://www.sanity.io/docs/developer-guides/add-analytics-to-sanity-studio): How to inject analytics scripts like Google Tag Manager into a Sanity Studio, including Sanity-hosted deployments.
- [How to pitch Sanity.io to your team](https://www.sanity.io/docs/developer-guides/how-to-pitch-sanity-io-to-your-team): Need help to convince your developer team to build with Sanity.io? Here are some points that may be useful!
- [Sanity's non-profit plan](https://www.sanity.io/docs/platform-management/non-profit-plan): Sanity offers a heavily discounted non-profit plan for eligible non-profit organizations.
- [Agencies: Navigating the Spring 2025 Organization Changes](https://www.sanity.io/docs/developer-guides/agencies-navigating-the-spring-2025-organization-changes): How to handle the changes to Organizations and Projects in Sanity
- [How to generate massive amounts of demo content for Sanity](https://www.sanity.io/docs/developer-guides/create-fake-demo-content-with-sanity-cli): It can be useful for testing plugins, front ends, or other integrations to have a Sanity Studio populated with fake content.
- [How to implement Multi-tenancy with Sanity](https://www.sanity.io/docs/developer-guides/multi-tenancy-implementation): In this guide, you’ll see how Sanity separates organizations, projects, datasets, and members by working through a hypothetical example of a growing company that can expand its content model as they grow – without needing a complete overhaul.
- [GROQ-Powered Webhooks – Intro to Filters](https://www.sanity.io/docs/developer-guides/filters-in-groq-powered-webhooks): A thorough intro to using GROQ-filters in a webhook-context
- [GROQ-Powered Webhooks – Intro to Projections](https://www.sanity.io/docs/developer-guides/projections-in-groq-powered-webhooks): A thorough intro to using GROQ-projections in a webhook contest
- [Presenting Portable Text](https://www.sanity.io/docs/developer-guides/presenting-block-text): Transform Portable Text to whatever you want
- [Add Inline blocks for the Portable Text Editor](https://www.sanity.io/docs/developer-guides/add-inline-blocks-to-portable-text-editor): Enrich your content and add inline blocks to your Portable Text Editor. This guide takes you from schema to query output
- [Beginners guide to Portable Text](https://www.sanity.io/docs/developer-guides/beginners-guide-to-portable-text): Discover the power of Portable Text with this essential guide. From data structure, serialisation to validation strategies, you'll learn everything you need to harness its potential.
- [How to add custom YouTube blocks to Portable Text](https://www.sanity.io/docs/developer-guides/portable-text-how-to-add-a-custom-youtube-embed-block): How to add a YouTube embed in the Studio, and render it on front ends
- [Converting Inline Styles to Sanity Block Decorators](https://www.sanity.io/docs/developer-guides/converting-inline-styles-to-sanity-block-decorators): Learn how to seamlessly migrate rich text with inline styles (like bold, italic, and underline) into Sanity block content. This guide provides a step-by-step solution to handle custom deserialization, including nested spans and advanced inline styles.
- [Adding things to Portable Text - From block content schema to React component](https://www.sanity.io/docs/developer-guides/ultimate-guide-for-customising-portable-text-from-schema-to-react-component): This Guide will lead you through the all the steps you need to level-up your use of Portable Text: from setting up block content, adding custom blocks and renderers for the Portable Text Editor in your studio. But also help you query for everything and render your awesome content in React!
- [Change the height of a Portable Text Editor (PTE) using a custom input component](https://www.sanity.io/docs/developer-guides/change-the-height-of-a-portable-text-editor-pte-using-a-custom-input-component): Ever used a PTE and thought you would like it to take up less space and be focusable without activating it? Now you can!
- [Create your own Sanity template](https://www.sanity.io/docs/developer-guides/create-your-own-sanity-template): Guide on creating, validating, and submitting a Sanity template for community use.
- [Community Code of Conduct](https://www.sanity.io/docs/developer-guides/community-code-of-conduct): This is the Code of Conduct that details the expected and unacceptable behaviors when participating in Sanity events or community spaces.
- [Migrating plugins to support Content Releases](https://www.sanity.io/docs/developer-guides/migrating-plugins-to-support-content-releases): Guide to support Content Releases and Perspectives in Studio plugins

### Getting started

- [Getting started with Sanity](https://www.sanity.io/docs/getting-started): Sanity is a fully customizeable all-code backend for all your content-driven websites and apps—their builders and creators.

From here you can explore the different ways of getting started: framework-specific quickstarts, templates, courses, or exploring the documentation.
- [A very short introduction](https://www.sanity.io/docs/getting-started/the-sanity-content-operating-system-an-introduction): Sanity is the back-end built for AI content operations. Power web, mobile, and agentic applications at scale.
- [What is AI-powered content operations?](https://www.sanity.io/docs/getting-started/what-is-content-operations): The Sanity Content Operating System is the intelligent backend for AI content operations at scale.
