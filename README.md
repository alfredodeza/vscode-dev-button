# Create an Open in VSCode.dev button

With the button you can add it to any GitHub repository and get reidrected to its VSCode.dev environment.

This is an Azure Function that you can use to add a button to a repository and get to VSCode.dev

**Note:** The current deployment uses _a personal Azure subscription_ attached to a domain, so don't rely on it working or for production use.

Current link: [https://vscode-dev.azurewebsites.net/](https://vscode-dev.azurewebsites.net/)

## Example badge usage:

Using shields.io :


```markdown
[![Open in VSCode.dev](https://img.shields.io/static/v1?label=Open%20In&message=VSCode.dev&labelColor=fff&color=444&logo=visualstudiocode&logoColor=blue)](https://vscode-dev.azurewebsites.net/)
```

Example output button (which redirects to this current repo):

[![Open in VSCode.dev](https://img.shields.io/static/v1?label=Open%20In&message=VSCode.dev&labelColor=fff&color=444&logo=visualstudiocode&logoColor=blue)](https://vscode-dev.azurewebsites.net/)


## Logic

The way this works is by poking at the header in the request. GitHub will add a `"Referer"`, so the function will look at that value for processing. If the value comes from a GitHub domain, then it will strip the url and redirect to VSCode.dev. For example the following url:

```
https://github.com/alfredodeza/vscode-dev-button
```

Will be converted into:

```
https://vscode.dev/github/alfredodeza/vscode-dev-button
```

If a `"Referer"` is not found, then it will just point to [VSCode.dev](https://vscode.dev) directly.
