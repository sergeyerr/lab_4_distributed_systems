<script>
    import { link, navigate } from "svelte-routing";
    import Card from "smelte/src/components/Card";
    import Button from "smelte/src/components/Button";
    import ProgressCircular from 'smelte/src/components/ProgressCircular';
    import { flip } from 'svelte/animate';
    import { onMount } from "svelte";
    import { user } from "../../lib/user.js";

    function sellStock(item) {
        $user.selectedStocks = $user.selectedStocks.filter(
            (s) => item.code !== s.code
        );
    }

    $: sortedStocks = ((stocks) => {
        return stocks
            .slice()
            .sort((sA, sB) => sA.name <= sB.name ? -1 : 0);
    })($user.selectedStocks);

    let state = '';

    onMount(() => {
        if ($user.name == null) {
            navigate("/signup");
        }
    });
</script>

<div class="flex mx-auto flex-col items-center">
    <h3 class="mx-auto">Suitcase</h3>
    <p class="mb-4">The <i>stonks</i> you bought end up here...</p>
    {#if state === 'loading'}
        <div class="m-auto">
            <ProgressCircular/>
        </div>
    {:else if $user.selectedStocks.length == 0}
        <div class="flex flex-col m-auto items-center">
            <div class="bg-orang bg-contain bg-center bg-no-repeat h-64 w-64" />
            <p>It appears yout suitcase is empty...</p>
            <p>
                You can buy some
                <i>stonks</i>
                over in the
                <a
                    use:link
                    class="text-secondary-300 hover:underline"
                    href="/stocks">
                    stonks
                </a>
                section!
            </p>
        </div>
    {:else}
        <div class="flex flex-wrap mx-32 justify-center my-auto">
            {#each sortedStocks as item (item.code)}
                <div animate:flip={{duration: 300}}>
                    <Card.Card class="mb-4 mr-4">
                        <div slot="title">
                            <Card.Title title={item.code} subheader={item.organization}/>
                        </div>
                        <div slot="text" class="px-4 pb-0 pt-0 text-right">
                            <span class="mr-8">${item.price}</span>
                            {#await item.variance()}
                                ...
                            {:then v}
                                <span>VAR {v}</span>
                            {:catch e}
                                <span>{e.message}</span>
                            {/await}
                        </div>
                        <div slot="actions" class="flex justify-center">
                            <div class="p-2">
                                <Button
                                    text
                                    on:click={sellStock(item)}
                                    add="text-secondary-300">
                                    Sell
                                </Button>
                            </div>
                        </div>
                    </Card.Card>
                </div>
            {/each}
        </div>
        <p>Buy more
            <a use:link href="/stocks" class="hover:underline text-secondary-300">
                stonks
            </a>
        </p>
    {/if}
</div>