# django-neotest

[Neotest](https://github.com/rcarriga/neotest) adapter for python.
Supports Pytest, DjangoUnitTest and unittest test files.

Requires [nvim-treesitter](https://github.com/nvim-treesitter/nvim-treesitter) and the parser for python.

**Lazy**

```lua
{
  "nvim-neotest/neotest",
  dependencies = {
    ...
    "kenunq/django-neotest",
  },
  config = function()
    require("neotest").setup({
      adapters = {
        require("django-neotest"),
      },
    })
  end,
}

```

You can optionally supply configuration settings:

```lua
require("neotest").setup({
  adapters = {
    require("django-neotest")({
        -- Extra arguments for nvim-dap configuration
        -- See https://github.com/microsoft/debugpy/wiki/Debug-configuration-settings for values
        dap = { justMyCode = false },
        -- Command line arguments for runner
        -- Can also be a function to return dynamic values
        args = {"--log-level", "DEBUG"},
        -- Runner to use. Will use pytest if available by default.
        -- Can be a function to return dynamic value.
        runner = "pytest", -- or "django", "unittest"
        -- Custom python path for the runner.
        -- Can be a string or a list of strings.
        -- Can also be a function to return dynamic value.
        -- If not provided, the path will be inferred by checking for
        -- virtual envs in the local directory and for Pipenev/Poetry configs
        python = ".venv/bin/python",
        -- Returns if a given file path is a test file.
        -- NB: This function is called a lot so don't perform any heavy tasks within it.
        is_test_file = function(file_path)
          ...
        end,
        -- !!EXPERIMENTAL!! Enable shelling out to `pytest` to discover test
        -- instances for files containing a parametrize mark (default: false)
        pytest_discover_instances = true,
    })
  }
})

```

For pytest you need create `pytest.ini`

```
[pytest]

DJANGO_SETTINGS_MODULE=mysite.settings

```

The adapter finds test files with the name: startwith - `"test_.py"`, endwith - `"_test.py"`, `"tests.py"`
