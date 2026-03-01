{
  description = "Project templates (devShells)";

  outputs = { self, ... }: {
    templates.uv-qt = {
      path = ./templates/uv-qt;
      description = "uv + PySide6 (Qt) devShell template";
    };

    # Add more as you make them:
    # templates.rust = { path = ./templates/rust; description = "..."; };

    templates.default = self.templates.uv-qt;
  };
}
