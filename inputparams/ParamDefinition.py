class ParamDefinition:

    def __init__(
            self,
            name: str,
            short_name: str,
            param_type: type,
            default=None,
            param_help: str = None
    ):
        self.name = name
        self.short_name = short_name
        self.type = param_type
        self.default = default
        self.help = param_help
