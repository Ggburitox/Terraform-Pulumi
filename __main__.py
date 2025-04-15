ami_id = "ami-022ce79dc9cabea0c" "Codigo de la AMI Cloud9ubuntu22"
key_name = "vockey"

sec_group = aws.ec2.SecurityGroup("mv-pulumi-sg",
    description="Allow SSH and HTTP traffic",
    ingress=[
        {"protocol": "tcp", "from_port": 22, "to_port": 22, "cidr_blocks": ["0.0.0.0/0"]},
        {"protocol": "tcp", "from_port": 80, "to_port": 80, "cidr_blocks": ["0.0.0.0/0"]},
    ],
    egress=[
        {"protocol": "-1", "from_port": 0, "to_port": 0, "cidr_blocks": ["0.0.0.0/0"]},
    ]
)

instance = aws.ec2.Instance("MV-PULUMI",
    instance_type="t2.micro",
    ami=ami_id,
    key_name=key_name,
    vpc_security_group_ids=[sec_group.id],
    tags={"Name": "MV-PULUMI"},
    root_block_device={"volume_size": 20}
)

pulumi.export("public_ip", instance.public_ip)
pulumi.export("instance_id", instance.id)
