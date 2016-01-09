Playbook to ease the profiling of containerized processes. A 
`profile_args` variable is expected, which corresponds to a list of 
`profile` invocations, where each element in the list is a string with 
the arguments to pass to `profile`. For example:

```bash
ansible-playbook -e \
'{ "profile_args": \
   [ "-f \"--net=host\" -i debian:jessie -c \"ping google.com -c 2 \" -n ping", \
     "-f \"-m 1G\"      -i debian:jessie -c \"stat / \"               -n stat" \
   ]\
 }' playbook.yml
```

The above profiles, on every host specified in `/etc/ansible/hosts`, 
the two commands shown above (`ping` and `stat`).
