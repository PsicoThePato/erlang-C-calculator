import math


def pi_zero(rho, n_containers, type='c'):
    def summer_gen(rho, n_containers):
        factorial_start = 1
        for i in range(n_containers):
            yield rho**i/factorial_start
            factorial_start = factorial_start * (i+1)
    summed_result = sum(summer_gen(rho, n_containers))
    second_result = (rho**n_containers/math.factorial(n_containers)) * \
        rho/(n_containers - rho)
    if type == 'b':
        second_result = 0
    return (summed_result + second_result)


def erlang(rho, n_containers, type='c'):
    steady_state_mult1 = (rho**n_containers)/math.factorial(n_containers)
    steady_state_mult2 = n_containers/(n_containers-rho)
    pi_zero_prob = pi_zero(rho, n_containers, 'c')
    return (steady_state_mult1 * steady_state_mult2)/pi_zero_prob


if __name__ == '__main__':
    RHO = 30
    N_CONTAINERS = 31
    SERVICE_TIME = 10
    divisor = SERVICE_TIME * (N_CONTAINERS - RHO)
    erlang_prob = erlang(RHO, N_CONTAINERS)
    print(erlang_prob)
    print((erlang_prob/(divisor)) + SERVICE_TIME)

    #erlang_prob = erlang(RHO, N_CONTAINERS, 'c')
    #print(erlang_prob)
