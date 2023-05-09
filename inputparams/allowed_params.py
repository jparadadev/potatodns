from inputparams.ParamDefinition import ParamDefinition


def get_params_definitions() -> list[ParamDefinition]:
    return [
        ParamDefinition('destiny', 'dst', str, '127.0.0.1', 'Default destiny for DNS packets.'),
        ParamDefinition('interface', 'I', str, 'en0', 'Default interface to sniff.'),
    ]
